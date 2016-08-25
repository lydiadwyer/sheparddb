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

        self.assertIn('Cyprus', result.data)
        self.assertIn('France', result.data)
        self.assertIn('Turkey', result.data)
        self.assertIn('<a href="/countries/add">add country</a>', result.data)

    def test_country_view1(self):

        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.app.get('/countries/view/1')

        self.assertIn('Cyprus', result.data)



    def test_country_add(self):

        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.app.get('/countries/add')
        print result.data

        self.assertIn('Add A Country', result.data)
        self.assertIn('Country Name', result.data)
        self.assertIn('Country Abbreviation', result.data)

    def test_country_add_valid(self):


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

        self.assertIn('<h1>Greece</h1>', result.data)
        self.assertIn('<a href="/countries/edit/4">Edit</a>', result.data)
        self.assertIn('<a href="/countries/delete/4">Delete</a>', result.data)

    def test_country_add_invalid(self):
        # ensure response is invalid


        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.app.post(
            '/countries/add',
            data={
                  'country_name': 'Greec1',
                  'country_abrev': ''
            },
            follow_redirects=True
        )
        # print result.data

        self.assertIn('<h1>Add A Country</h1>', result.data)
        self.assertIn('<span id="country_name_msg" class="error_msg">Please fill in a country name only with English letters.</span>',
                       result.data)
        self.assertIn('<span id="country_abrev_msg" class="error_msg">Please fill in the country abbreviation with 2 characters.</span>',
                       result.data)


    def test_country_edit3(self):

        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.app.get('/countries/edit/3')

        self.assertIn('Turkey', result.data)

    def test_country_edit_valid(self):


        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.app.post(
            '/countries/edit/3',
            data={
                  'country_name': 'Turkey',
                  'country_abrev': 'TR'
            },
            follow_redirects=True
        )
        # print result.data

        self.assertIn('<h1>Turkey</h1>', result.data)
        self.assertIn('<td>Turkey</td>', result.data)
        self.assertIn('<td>TR</td>', result.data)
        self.assertIn('<a href="/countries/edit/3">Edit</a>', result.data)
        self.assertIn('<a href="/countries/delete/3">Delete</a>', result.data)


    def test_country_edit_invalid(self):
        # ensure response is invalid


        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.app.post(
            '/countries/edit/3',
            data={
                  'country_name': 'Turk8',
                  'country_abrev': ''
            },
            follow_redirects=True
        )
        # print result.data

        self.assertIn('<span id="country_name_msg" class="error_msg">Please fill in a country name only with English letters.</span>',
                       result.data)
        self.assertIn('<span id="country_abrev_msg" class="error_msg">Please fill in the country abbreviation with 2 characters.</span>',
                       result.data)

    def test_country_delete(self):
        # ensure entry is deleted
        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.app.post(
            '/countries/delete/2',
            data={
                  'country_name': 'Turk8',
                  'country_abrev': ''
            },
            follow_redirects=True
        )
        # print result.data

        self.assertIn('',
                       result.data)
        self.assertIn('',
                       result.data)






if __name__ == '__main__':
    unittest.main()
