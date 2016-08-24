import os
from shepard import app
import unittest
import tempfile
import subprocess, os, time

# http://flask.pocoo.org/docs/0.11/testing/
# https://docs.python.org/2/library/unittest.html#assert-methods
class CountryTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # self.reset_database()


    def tearDown(self):
        pass

    def test_country_default(self):

        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.app.get('/countries/')

        self.assertEqual(result.status_code, 200)
        self.assertIn('Cyprus', result.data)
        self.assertIn('France', result.data)
        self.assertIn('Turkey', result.data)
        self.assertIn('<a href="/countries/add">add country</a>', result.data)

    def test_country_add(self):

        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.app.get('/countries/add')

        self.assertEqual(result.status_code, 200)
        self.assertIn('Add A Country', result.data)
        self.assertIn('Country Name', result.data)
        self.assertIn('Country Abbreviation', result.data)

    def test_country_add_valid(self):

        return True

        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.app.post(
            '/countries/add',
            data={
                  'country_name': 'Greece',
                  'country_abrev': 'GR'
            },
            follow_redirects=True
        )
        # print result.data

        self.assertEqual(result.status_code, 200)
        self.assertIn('<h1>Greece</h1>', result.data)
        self.assertIn('<a href="/countries/edit/4">Edit</a>', result.data)
        self.assertIn('<a href="/countries/delete/4">Delete</a>', result.data)





if __name__ == '__main__':
    unittest.main()
