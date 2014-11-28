from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pytz import timezone
from flask import request, session
from app import app, db
from models import User


# Used by template to render all page content
class Content(object):
    delta = None

    def __init__(self, tz):
        self.tz = tz

    @property
    def heading(self):
        return 'heading'

    @property
    def subheading(self):
        return 'subheading'

    @property
    def desc(self):
        return 'desc'

    @property
    def months(self):
        if self.delta.years > 0:
            return self.delta.years*12 + self.delta.months
        return self.delta.months


def get_content(year=None, month=None, day=None, event=None):
    tz = timezone(session.get('tz', app.config['DEFAULT_TZ']))
    c = Content(tz)
    l_now = tz.localize(datetime.now())
    # DMY based
    if year is not None:
        l_date = tz.localize(datetime(int(year), int(month), int(day), 0, 0, 0))
        c.delta = relativedelta(l_date, l_now)
        c.date = l_date
        return c
    # Event based
    if event is not None:
        return c