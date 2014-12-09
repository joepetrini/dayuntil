from datetime import datetime
import random
from flask import request
from flask.ext.mail import Message
from app import app, mail
from config import ADMINS



def _t(template_name):
    if request.MOBILE:
        return "mob_%s" % template_name
    return template_name


def email(subj, msg):
    msg = Message(subj, sender=ADMINS[0], recipients=ADMINS)
    msg.body = msg
    with app.app_context():
        mail.send(msg)


# Used for A/B testing
def _ab(pct_split=50):
    if random.random() < (pct_split / 100.00):
        return True#return 'a'
    else:
        return False#return 'b'