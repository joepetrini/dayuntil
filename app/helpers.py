from flask import request
import requests

def _t(template_name):
    print request.MOBILE
    return template_name


def get_token(app_id, app_secret, short_lived_token):
    url = '/oauth/access_token?grant_type=fb_exchange_token&client_id=%s' \
          "&client_secret=%s&fb_exchange_token=%s" % (app_id, app_secret, short_lived_token)
    pass