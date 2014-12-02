from werkzeug.utils import import_string
from app import db
from app.models import Day


#ids = set([u.id for u in Day.query.all()])
import_string('app.holidays')
