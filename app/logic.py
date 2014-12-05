from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pytz import timezone
import redis
from flask import request, session
from app import app, db
from models import Day, Fact


# Used by template to render all page content
class Content(object):
    delta = None
    event = None
    date = None

    def __init__(self, tz):
        self.tz = tz

    @property
    def meta_keywords(self):
        if self.event:
            kw = "Days until %s %s, " % (self.event.name, self.date.year)
            kw += "Countdown until %s %s, " % (self.event.name, self.date.year)
            kw += "days until, how many days, how much time"
        else:
            kw = "Days until %s, " % self.date.strftime("%A %B %d %Y")
            kw += "Countdown until %s, " % self.date.strftime("%A %B %d %Y")
            kw += "days until, how many days, hours until, date calculator"
        return kw

    @property
    def meta_desc(self):
        if self.event:
            d = "Days until %s %s. " % (self.event.name, self.date.year)
            d += "Countdown until %s %s. " % (self.event.name, self.date.year)
            d += "DayUntil - Find out how many days left"
        else:
            d = "Days until %s. " % self.date.strftime("%A %B %d %Y")
            d += "Countdown until %s. " % self.date.strftime("%A %B %d %Y")
            d += "DayUntil - Find out how many days left"
        return d

    @property
    def title(self):
        if self.event:
            return "Days until %s %s" % (self.event.name, self.event.date.year)
        else:
            return "Days until %s" % self.date.strftime("%A %B %Y")

    @property
    def heading(self):
        return "%s days" % abs(self.delta.days)

    @property
    def subheading(self):
        if self.event:
            if self.delta.days > 0:
                return "Until %s %s" % (self.event.name, self.event.date.year)
            else:
                return "Since %s %s" % (self.event.name, self.event.date.year)
        else:
            if self.delta.days > 0:
                return "Until %s" % self.date.strftime("%B %d %Y")
            else:
                return "Since %s" % self.date.strftime("%B %d %Y")

    @property
    def desc(self):
        if self.event:
            return self.event.desc
        else:
            return ""
            #return "A %s" % (self.date.strftime("%A"), self.delta.months

    @property
    def months(self):
        if self.delta.years > 0:
            return self.delta.years*12 + self.delta.months
        return self.delta.months

    @property
    def nearby_events(self):
        return db.session.query(Day) \
            .filter(Day.date > self.date) \
            .order_by(Day.date).limit(5)

    @property
    def fact(self):
        d = datetime(2000, self.date.month, self.date.day)
        f = Fact.query.filter_by(date=d).first()
        return f.text

    @property
    def link(self):
        if self.event:
            return "<a href='%s'>%s</a>" % (self.event.link, self.event.link)


def get_content(year=None, month=None, day=None, event=None):
    tz = timezone(session.get('tz', app.config['DEFAULT_TZ']))
    c = Content(tz)
    l_now = tz.localize(datetime.now())
    # DMY based
    if year is not None:
        l_date = tz.localize(datetime(int(year), int(month), int(day), 0, 0, 0))
    # Event based
    if event is not None:
        l_date = tz.localize(event.date)
    c.date = l_date
    c.rdelta = relativedelta(l_date, l_now)
    c.delta = l_date - l_now
    c.event = event
    return c


def get_sitemap():
    s = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    s += "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"

    # Data driven events
    sys_names = set([d.sys_name for d in Day.query.all()])
    for name in sys_names:
        s += "\t<url>\n"
        s += "\t\t<loc>http://%s/%s</loc>\n" % ('www.dayuntil.com', name)
        s += "\t\t<changefreq>daily</changefreq>\n"
        s += "\t</url>\n"

    # TODO switch up loop to go by year, not day type to test SEO
    for d in Day.query.all():
        s += "\t<url>\n"
        s += "\t\t<loc>http://%s/%s</loc>\n" % ('www.dayuntil.com', d.id)
        s += "\t\t<changefreq>daily</changefreq>\n"
        s += "\t</url>\n"


    # Go 3 years into the future for regular dates
    now = datetime.today() - timedelta(days=180)
    for i in range(0, 1180):
        d = now + timedelta(days=i)
        ds = "%02d/%02d/%s" % (d.month, d.day, d.year)
        s += "\t<url>\n"
        s += "\t\t<loc>http://%s/%s</loc>\n" % ('www.dayuntil.com', ds)
        s += "\t\t<changefreq>daily</changefreq>\n"
        s += "\t</url>\n"

    s += "</urlset>\n"
    return s