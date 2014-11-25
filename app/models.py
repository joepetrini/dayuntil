#from flask.ext.security import UserMixin, RoleMixin
from sqlalchemy_utils import Timestamp
from . import db


class User(db.Model, Timestamp):
    __tablename__ = "users"

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    profile_url = db.Column(db.String)
    #email = db.Column(db.String(255), unique=True)
    #password = db.Column(db.String(120))
    #active = db.Column(db.Boolean())
    last_login = db.Column(db.DateTime())
    #last_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer, default=1)
    #created = db.Column(db.DateTime())

