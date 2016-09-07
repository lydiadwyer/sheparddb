#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import psycopg2
from flask_testing import TestCase
from shepard import create_flask


# http://flask.pocoo.org/docs/0.11/testing/
# http://flask.pocoo.org/docs/0.11/api/#flask.Response
# https://docs.python.org/2/library/unittest.html#assert-methods
# Tests most forms and validation, can be used for other forms
class BaseTestCase(TestCase):
    """ A base test case to use with other test modules """

    def reset_database(self):
<<<<<<< HEAD:data/website/test/BaseTestCase.py
=======

        print 'BaseTestCase::resetting...'

>>>>>>> 738ddc840e4455b424568474d2e169b2e79065bc:data/website/stuff/BaseTestCase.py
        conn = psycopg2.connect(
            "dbname=sheparddb user=shepard host=127.0.0.1 password=shepard")
        conn.autocommit = True
        cursor = conn.cursor()
#        cursor.execute("DROP SCHEMA IF EXISTS sheparddb CASCADE;")
        cursor.execute(open("/vagrant/psql/db_create_schema.sql", "r").read())
        cursor.execute(open("/vagrant/psql/db_data.sql", "r").read())
        cursor.close()
        conn.close()     

<<<<<<< HEAD:data/website/test/BaseTestCase.py
    def setUp(self):
        self.reset_database()       
        self.app = app.test_client()
        self.app.testing = True
        
    # do suit of tests?
=======
    def create_app(self):
        print 'BaseTestCase::create_app()'
        app = create_flask()
        app.config['TESTING'] = True
        app.testing = True
        # app = app.test_client()
        return app

    def setUp(self):
        self.reset_database()
        self.app = self.create_app()
        pass
>>>>>>> 738ddc840e4455b424568474d2e169b2e79065bc:data/website/stuff/BaseTestCase.py

    def tearDown(self):
        pass
