import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from datetime import datetime
import StringIO
import csv
import redis
import requests
from app import db
import config
from app.models import Day


red = redis.Redis()
s = ""
key = "sheet_%s" % config.GSHEET_KEY
if red.get(key) is None:
    url = "https://docs.google.com/spreadsheet/ccc?key=%s&output=csv" % config.GSHEET_KEY
    s = requests.get(url).content
    red.setex(key, s, 3600)  # 1 Hour
else:
    s = red.get(key)

ids = set([u.id for u in Day.query.all()])

f = StringIO.StringIO(s)
rows = list(csv.reader(f, delimiter=','))
for row in rows[1:]:
    id = str(row[0]).lower()
    sys_name = str(row[1]).lower()
    name = row[2]
    priority = row[8]
    desc = row[4]
    alt_names = row[3]
    link = row[5]
    link_title = row[6]
    date = datetime.strptime(row[7], '%Y-%m-%d')
    if id not in ids:
        print "creating %s" % id
        d = Day(id=id, sys_name=sys_name, name=name, date=date)
        d.priority = priority
        db.session.add(d)
    else:
        print "%s found, updating" % id
        d = Day.query.get(id)

    d.sys_name = sys_name
    d.name = name
    d.date = date
    d.priority = priority
    print "setting desc to %s" % desc
    d.desc = desc
    d.alt_names = alt_names
    d.link = link
    d.link_title = link_title
    db.session.commit()
