from datetime import datetime
import random
from flask import request
from flask.ext.mail import Message
from app import app, mail
from config import ADMINS, DEBUG, MAIL_FROM



def _t(template_name):
    if request.MOBILE:
        return "mob_%s" % template_name
    return template_name


def ordinal(num):
    if 4 <= num <= 20 or 24 <= num <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][num % 10 - 1]
    return "%s%s" % (num, suffix)


def email(subj, content):
    msg = Message(subj, sender=MAIL_FROM, recipients=ADMINS)
    msg.body = content
    if DEBUG:
        print "DEBUG: Email %s" % content
    else:
        with app.app_context():
            mail.send(msg)


# Used for A/B testing
def _ab(pct_split=50):
    if random.random() < (pct_split / 100.00):
        return True#return 'a'
    else:
        return False#return 'b'