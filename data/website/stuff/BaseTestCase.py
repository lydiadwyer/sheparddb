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

        print 'BaseTestCase::resetting...'

        conn = psycopg2.connect(
            "dbname=sheparddb user=shepard host=127.0.0.1 password=shepard")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(open("/vagrant/psql/db_create_schema.sql", "r").read())
        cursor.execute(open("/vagrant/psql/db_data.sql", "r").read())
        cursor.close()
        conn.close()

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

    def tearDown(self):
        pass
