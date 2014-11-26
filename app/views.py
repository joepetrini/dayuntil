from flask import flash, g, redirect, current_app, render_template, request, url_for, session
from facebook import get_user_from_cookie, GraphAPI
#from flask.ext.security import LoginForm, current_user, login_required, login_user
from app import app
from helpers import _t
from logic import *


#@app.context_processor
#def template_extras():
#    return dict(google_analytics_id=app.config.get('GOOGLE_ANALYTICS_ID', None))


@app.route('/')
def index():
    return render_template(_t('landing.html'))


@app.route('/sitemap.xml')
def sitemap():
    return ""


@app.route('/<month>/<day>/<year>')
def mdy(day, month, year):
    content = get_content(year=year, month=month, day=day)
    return render_template(_t('day.html'), c=content)


@app.route('/e/<event_name>')
def event(event_name):
    content = get_content(event=event_name)
    return render_template(_t('day.html'), c=content)


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
    # Set the user in the session dictionary as a global g.user and bail out
    # of this function early.
    if session.get('user'):
        g.user = session.get('user')
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
                               id=user.id, access_token=user.access_token)

    # Commit changes to the database and set the user as a global g.user
    db.session.commit()
    g.user = session.get('user', None)
