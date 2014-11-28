import sys, json
from werkzeug.utils import import_string
from sqlalchemy import and_, exc
from flask.ext.script import Manager
from flask import g
from app import app, db
from app.models import Day
#from app.logic import create_card
#from app.trello import Trello
#from app.helpers import utc_now
from app.holidays import *
import redis
import requests


manager = Manager(app)


@manager.command
def days_from_webcal():
    r = redis.Redis()
    ids = [424, 50, 221, 52, 342, 335, 208, 45, 44]
    url = 'http://www.webcal.fi/cal.php?id=%s&format=json&start_year=previous_year&end_year=2019&tz=UTC'
    for i in ids:
        u = url % i
        t = r.get(u)
        if t is None:
            t = requests.get

        print u
        break


@manager.command
def create_days():
    ids = set([u.id for u in Day.query.all()])
    for y in range(2010, 2025):

        ####################
        ####### Summer #####
        ####################
        a = {2012: '6-20', 2013: '6-21', 2014: '6-21', 2015: '6-21', 2016: '6-20', 2017: '6-21', 2018: '6-21', 2019: '6-21',
         2020: '6-20'}
        if a.has_key(y):
            d = a[y].split('-')
            dt = datetime(int(y), int(d[0]), int(d[1]))
            id = 'summer-%s' % y
            if id in ids: continue;
            day = Day(id=id, sys_name='summer', name="Summer", date=dt)
            db.session.add(day)

        ####################
        ####### Fall ######
        ####################
        a = {2012: '9-23', 2013: '9-22', 2014: '9-23', 2015: '9-23', 2016: '9-22', 2016: '9-22', 2018: '9-23', 2019: '9-23',
         2020: '9-22'}
        if a.has_key(y):
            d = a[y].split('-')
            dt = datetime(int(y), int(d[0]), int(d[1]))
            id = 'fall-%s' % y
            if id in ids: continue;
            day = Day(id=id, sys_name='fall', name="Fall", date=dt)
            db.session.add(day)


        ####################
        ####### Winter #####
        ####################
        a = {2012: '12-21', 2013: '12-21', 2014: '12-21', 2015: '12-22', 2016: '12-21', 2017: '12-21', 2018: '12-21',
         2019: '12-22', 2020: '12-21'}
        if a.has_key(y):
            d = a[y].split('-')
            dt = datetime(int(y), int(d[0]), int(d[1]))
            id = 'winter-%s' % y
            if id in ids: continue;
            day = Day(id=id, sys_name='winter', name="Winter", date=dt)
            db.session.add(day)


        ####################
        ####### Spring #####
        ####################
        dt = datetime(int(y), 3, 20)
        id = 'spring-%s' % y
        if id in ids: continue;
        day = Day(id=id, sys_name='spring', name="Spring", date=dt)
        db.session.add(day)


    db.session.commit()


if __name__ == "__main__":
    manager.run()