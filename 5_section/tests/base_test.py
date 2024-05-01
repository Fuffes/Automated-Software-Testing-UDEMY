"""
BaseTest

This class should be the parent class to each non-unit test.
It allows instantiation of the database dynamically
and makes sure that it is a new, blanc database each time

"""

import unittest
from app import app
from db import db

class BaseTest(unittest.TestCase):
    def setUp(self):
        """set database"""
        app.config["SQLACCHEMY_DATABASE_URI"] = "sqlite:///"
        with app.app_context():
            db.init_app(app)
            db.create_all()
        self.app = app.test_client()
        self.app_context = app.app_context()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

