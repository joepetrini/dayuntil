import datetime
import re
from flask import flash, g, redirect, current_app, render_template, request, url_for, session
from facebook import get_user_from_cookie, GraphAPI
#from flask.ext.security import LoginForm, current_user, login_required, login_user
from app import app
from helpers import _ab, email, ordinal
from logic import *
from models import Day, User, UserDay


#@app.context_processor
#def template_extras():
#    return dict(google_analytics_id=app.config.get('GOOGLE_ANALYTICS_ID', None))


@app.route('/')
def index():
    events = db.session.query(Day) \
        .filter(Day.date > datetime.today()) \
        .filter(Day.priority > 50) \
        .order_by(Day.date).limit(10)
    years = range(datetime.today().year, datetime.today().year + 10)
    return render_template('landing.html', days=events, years=years)


@app.route('/sitemap.xml')
def sitemap():
    return get_sitemap()


@app.route('/api/add', methods=['POST'])
def add_day():
    if not g.user:
        return "ERROR"
    name = request.form['name']
    date = request.form['date']
    d = UserDay(name=name, date=date, user=g.user)
    db.session.add(d)
    db.session.commit()
    return render_template('_userday.html', day=d)


@app.route('/api/remove', methods=['POST'])
def remove_day():
    if not g.user:
        return "ERROR"
    date = request.form['date']
    day = db.session.query(UserDay) \
        .filter(UserDay.user == g.user) \
        .filter(UserDay.date == date).first()
    db.session.delete(day)
    db.session.commit()
    return ''


@app.route('/admin')
def admin():
    if g.user['admin']:
        users = User.query.all()
        return render_template('admin.html', users=users)
    return ''


@app.route('/<int:month>/<int:day>/<int:year>')
def mdy(day, month, year):
    content = get_content(year=year, month=month, day=day, user=g.user)
    return render_template('day.html', c=content)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    success = False
    if request.method == 'POST':
        name = request.form['email']
        message = "%s - %s" % (name, request.form['message'])
        email("Contact form submission", message)
        success = True
    return render_template('contact.html', success=success)


@app.route('/month/<month_name>')
def month(month_name):
    months = months_dict()
    mnum = months[month_name.lower()]
    mord = ordinal(mnum)
    day_count = calendar.monthrange(2000, mnum)[1]
    days = db.session.query(Day) \
        .filter(Day.date > datetime.today()) \
        .filter(Day.date < datetime.today() + timedelta(days=365))
    return render_template('month.html', m=month_name, days=days, count=day_count, month=mnum, mord=mord, months=months)


@app.route('/<day_name>')
def event(day_name):
    if '.' in day_name:
        return ""
    show_year = True
    # Year in url, easy
    if re.search('-\d{4}', day_name[-5:]):
        #m = re.search('([^\d]+)(\d{4})', day_name)
        print day_name
        day = Day.query.get(day_name.lower())
    # No year, pick next nearest by sys_name
    else:
        day = db.session.query(Day) \
            .filter(Day.sys_name == str(day_name)) \
            .filter(Day.date > datetime.today()).first()
        show_year = False
    content = get_content(event=day, show_year=show_year)
    day.add_view()
    db.session.commit()
    return render_template('day.html', c=content)


@app.route('/api/timezone')
def api_timezone():
    tz = request.args.get('tz')
    session['tz'] = tz
    return tz


@app.route('/logout')
def logout():
    """
    Log out the user from the application.
    Log out the user from the application by removing them from the
    session.  Note: this does not log the user out of Facebook - this is done
    by the JavaScript SDK.
    """
    session.pop('user', None)
    return redirect(url_for('index'))


@app.before_request
def get_current_user():
    """Set g.user to the currently logged in user.

    Called before each request, get_current_user sets the global g.user
    variable to the currently logged in user.  A currently logged in user is
    determined by seeing if it exists in Flask's session dictionary.

    If it is the first time the user is logging into this application it will
    create the user and insert it into the database.  If the user is not logged
    in, None will be set to g.user.
    """
    # A/B test value
    g.ab = _ab()

    # Set the user in the session dictionary as a global g.user and bail out
    # of this function early.
    if session.get('user'):
        user = session.get('user')
        user = User.query.filter(User.id == user['id']).first()
        g.user = user
        return



    # Attempt to get the short term access token for the current user.
    result = get_user_from_cookie(cookies=request.cookies, app_id=app.config['FB_APP_ID'],
                                  app_secret=app.config['FB_SECRET'])

    # If there is no result, we assume the user is not logged in.
    if result:
        # Check to see if this user is already in our database.
        user = User.query.filter(User.id == result['uid']).first()

        if not user:
            # Not an existing user so get info
            graph = GraphAPI(result['access_token'])
            profile = graph.get_object('me')

            # Create the user and insert it into the database
            user = User(id=str(profile['id']), name=profile['name'],
                        profile_url=profile['link'],
                        access_token=result['access_token'])
            db.session.add(user)
        elif user.access_token != result['access_token']:
            # If an existing user, update the access token
            user.access_token = result['access_token']

        # Add the user to the current session
        session['user'] = dict(name=user.name, profile_url=user.profile_url,
                               id=user.id, access_token=user.access_token,
                               admin=user.admin)

        # Commit changes to the database and set the user as a global g.user
        db.session.commit()
        g.user = session.get('user', None)
    else:
        g.user = None