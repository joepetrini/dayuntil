from datetime import datetime
import random
from flask import request


def _t(template_name):
    if request.MOBILE:
        return "mob_%s" % template_name
    return template_name


# Used for A/B testing
def _ab(pct_split=50):
    if random.random() < (pct_split / 100.00):
        return 'a'
    else:
        return 'b'