import os
from shepard import app
import unittest
import tempfile
import subprocess, os, time

# http://flask.pocoo.org/docs/0.11/testing/
# http://flask.pocoo.org/docs/0.11/api/#flask.Response
# https://docs.python.org/2/library/unittest.html#assert-methods
# Tests most forms and validation, can be used for other forms

class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # self.reset_database()


    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
