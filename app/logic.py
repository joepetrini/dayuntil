import datetime
import requests
import facebook
from app import app, db
from models import User


def get_or_create_user(user_id, token):
    user = User.query.filter_by(id=user_id).first()
    now = datetime.datetime.utcnow()

    # Existing user
    if user:
        user.last_login = now
        user.login_count += 1
    # New user
    else:
        app_id = app.config['FB_APP_ID']
        app_secret = app.config['FB_SECRET']
        url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s' \
              "&client_secret=%s&fb_exchange_token=%s" % (app_id, app_secret, token)
        r = requests.get(url)
        token = r.text.split('=')[1].split('&')[0]
        graph = facebook.GraphAPI(token)
        profile = graph.get_object('me')
        # email = profile['email'] # TODO
        name = profile['name']
        user = User(id=user_id, name=name, token=token, created=now, last_login=now)
        db.session.add(user)
    db.session.commit()
    return user