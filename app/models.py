#from flask.ext.security import UserMixin, RoleMixin
from sqlalchemy_utils import Timestamp
from sqlalchemy_utils.types.choice import ChoiceType
from . import db


class User(db.Model, Timestamp):
    __tablename__ = "users"

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    profile_url = db.Column(db.String(255))

    last_login = db.Column(db.DateTime())
    login_count = db.Column(db.Integer, default=1)

    #email = db.Column(db.String(255), unique=True)
    #password = db.Column(db.String(120))
    #active = db.Column(db.Boolean())


#class Concept(db.Model, Timestamp):
#    name =

class Day(db.Model, Timestamp):
    __tablename__ = "days"

    TYPES = [
        (u'holiday', u'Holiday'),
        (u'yr_event', u'Yearly event'),
        (u'one_time', u'One Time')
    ]

    # Slug field as PK
    id = db.Column(db.String(255), primary_key=True)
    sys_name = db.Column(db.String(255), index=True)
    name = db.Column(db.String(255))
    alt_names = db.Column(db.String(255), nullable=True)
    desc = db.Column(db.Text(), nullable=True)

    link = db.Column(db.String(1000), nullable=True)
    link_title = db.Column(db.String(255), nullable=True)

    #type = db.Column(ChoiceType(TYPES))

    # One off event types
    # one_time = bool # If false, dynamic look up date in holidays.py file
    date = db.Column(db.DateTime(), nullable=False)
    #date_end = db.Column(db.DateTime(), nullable=True)

    # Repeatabe
    # year = db.Column(db.Integer, nullable=True)
    priority = db.Column(db.Integer(), default=0)
    view_count = db.Column(db.Integer(), default=0)


class Fact(db.Model, Timestamp):
    __tablename__ = "facts"

    id = db.Column(db.Integer(), primary_key=True)
    source = db.Column(db.String(50))
    date = db.Column(db.DateTime(), nullable=False)
    text = db.Column(db.Text())
    active = db.Column(db.Boolean(), default=False)
    twitter_id = db.Column(db.String(100), nullable=True)

"""
To Handle:
 - Yearly holidays
 - Eventless seasons like Spring
 - Eventful season like TV
 - One off events like movie openings


Successive years of holidays are like episodes of a tv show
Weather seasons are like episode less seasons

Concept
 - Name

Season
 - concept FK
 - year/#
 - start
 - end

Event
 - season FK


How to handle ranges?  Olympics, seasons
"When do the olympics end"

class UserDates()
 - user
 - da
For non simple dates
 - holidays
 -



class Season
    name: "NHL 2014" or "Boardwalk empire Season 6"
    start
    end

class SeasonEvent
    name = "
    date =
"""