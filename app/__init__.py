import sys
from werkzeug.utils import import_string
from flask import Flask, redirect, url_for, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mobility import Mobility
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.migrate import Migrate

version = "0.1"
app = Flask(__name__)
Mobility(app)

# Check config has all values in config_copy_me
diff = set(dir(import_string('config_copyme'))) - set(dir(import_string('config')))
if len(diff) > 0:
    print "Abort!  Missing config values %s" % diff
    sys.exit(0)

app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

toolbar = DebugToolbarExtension(app)


# Late import so modules can import their dependencies properly
from . import models, views

#security_ds = SQLAlchemyUserDatastore(db, models.User, models.Role)
#social_ds = SQLAlchemyConnectionDatastore(db, models.Connection)

#app.security = Security(app, security_ds)
#app.social = Social(app, social_ds)
