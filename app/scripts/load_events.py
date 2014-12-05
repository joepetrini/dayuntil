import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from datetime import datetime
from werkzeug.utils import import_string
from app import db
from app.models import Day
import holidays


ids = set([u.id for u in Day.query.all()])

day_funcs = set([m for m in dir(import_string('holidays')) if m[-4:] == '_day'])

for y in range(datetime.today().year, datetime.today().year + 11):
    for d in day_funcs:
        meth = getattr(holidays, d)
        try:
            r = dict(meth(y))
        except KeyError:
            #print "KeyError: %s %s" % (d, y)
            continue
        # TODO Build sys name and ids
        name = r['name']
        date = r['date']
        sys_name = r.get('sys_name', name.replace(' ', '-').lower())
        priority = r.get('priority', 0)
        desc = str(r.get('desc', '')).strip()
        alt_names = r.get('alt_names', '')
        link = r.get('link', '')
        link_title = r.get('link_title', '')
        id = "%s-%s" % (sys_name, y)
        if id not in ids:
            print "creating %s" % id
            d = Day(id=id, sys_name=sys_name, name=name, date=date)
            d.priority = priority
            db.session.add(d)
        else:
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

