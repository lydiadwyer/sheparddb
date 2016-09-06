import os
from shepard import app
import unittest
import tempfile
import subprocess, os, time
import psycopg2

# http://flask.pocoo.org/docs/0.11/testing/
# http://flask.pocoo.org/docs/0.11/api/#flask.Response
# https://docs.python.org/2/library/unittest.html#assert-methods
# Tests most forms and validation, can be used for other forms
class BaseTestCase(unittest.TestCase):
    """ A base test case to use with other test modules """

    def reset_database(self):

        conn = psycopg2.connect(
            "dbname=sheparddb user=shepard host=127.0.0.1 password=shepard")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(open("/vagrant/psql/db_create_schema.sql", "r").read())
        cursor.execute(open("/vagrant/psql/db_data.sql", "r").read())
        cursor.close()
        conn.close()

    def setUp(self):
        self.reset_database()       
        self.app = app.test_client()
        self.app.testing = True


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
