import os
from datetime import datetime
import unittest
import pytz
from flask import url_for
from config import BASE_DIR
from app import app, db
from app.models import User
from app.logic import *


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a blank temp database before each test"""
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'deterministic'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'dtest.db')
        self.app = app.test_client()
        self.ctx = app.test_request_context()
        self.ctx.push()
        db.create_all()

        # Create some data
        #next = datetime(2000, 6, 1, 0, 0, 0).replace(tzinfo=pytz.utc)
        #offset = 60 * 4  # 4 hour offset
        #self.user = User(id='1', username='john', token='a', me_json='', tz_next_date=next, tz_offset_next=offset)
        #db.session.add(self.user)
        #db.session.commit()


    def tearDown(self):
        """Destroy blank temp database after each test"""
        db.session.remove()
        db.drop_all()


    def test_timezone(self):
        # Create a user with a timezone offset
        pass


if __name__ == '__main__':
    unittest.main()