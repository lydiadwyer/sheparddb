import os
from shepard import app, db
import tempfile
import subprocess, os, time
from flask.ext.testing import TestCase


# http://flask.pocoo.org/docs/0.11/testing/
# http://flask.pocoo.org/docs/0.11/api/#flask.Response
# https://docs.python.org/2/library/unittest.html#assert-methods
# Tests most forms and validation, can be used for other forms

class BaseTestCase(TestCase):
    """ A base test case to use with other test modules """
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()
        # self.reset_database()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
