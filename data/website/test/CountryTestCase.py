import subprocess, os, time, psycopg2
# from BaseTestCase import BaseTestCase
from flask_testing import TestCase
from shepard import create_flask

# http://flask.pocoo.org/docs/0.11/testing/
# http://flask.pocoo.org/docs/0.11/api/#flask.Response
# https://docs.python.org/2/library/unittest.html#assert-methods
class CountryTestCase(TestCase):

    def reset_database(self):

        print 'CountryTestCase::rest_database()'

        conn = psycopg2.connect(
            "dbname=sheparddb user=shepard host=127.0.0.1 password=shepard")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(open("/vagrant/psql/db_create_schema.sql", "r").read())
        cursor.execute(open("/vagrant/psql/db_data.sql", "r").read())
        cursor.close()
        conn.close()

    def create_app(self):
        # self.reset_database()
        print 'CountryTestCase::create_app()'
        app = create_flask()
        app.config['TESTING'] = True
        app.testing = True
        # app = app.test_client()
        return app

    def setUp(self):
        # self.reset_database()
        # self.app = self.create_app()
        pass

    def tearDown(self):
        pass

#data/website/test/flask_test_countries.py
    def test_country_default(self):

        result = self.client.get('/countries/')

        self.assertIn('Cyprus', result.data)
        self.assertIn('France', result.data)
        self.assertIn('Turkey', result.data)
        self.assertIn('<a href="/countries/add">Add country</a>', result.data)

    def test_country_view1(self):

        result = self.client.get('/countries/view/1')

        self.assertIn('Cyprus', result.data)

    def test_country_view_none(self):

        result = self.client.get(
            '/countries/view/99',
            follow_redirects=True
        )

        self.assertIn('Entry does not exist.', result.data)

    def test_country_add(self):

        result = self.client.get('/countries/add')

        self.assertIn('Add A Country', result.data)
        self.assertIn('Country Name', result.data)
        self.assertIn('Country Abbreviation', result.data)

    def test_country_add_valid(self):

        result = self.client.post(
            '/countries/add',
            data={
                  'country_name': 'Greece',
                  'country_abrev': 'GR'
            },
            follow_redirects=True
        )

        self.assertIn('<h1>Greece</h1>', result.data)
        self.assertIn('<td>Greece</td>', result.data)
        self.assertIn('<td>GR</td>', result.data)
        self.assertIn('Edit', result.data)
        self.assertIn('Delete', result.data)

    def test_country_add_invalid(self):

        result = self.client.post(
            '/countries/add',
            data={
                  'country_name': 'Greec1',
                  'country_abrev': 'gg'
            },
            follow_redirects=True
        )
        # print result.data

        self.assertIn('<h1>Add A Country</h1>', result.data)
        self.assertIn('Please fill in a country name only with English letters.',
                       result.data)
        self.assertIn('Please fill in the country abbreviation using only uppercase letters.',
                       result.data)


    def test_country_edit3(self):

        result = self.client.get('/countries/edit/3')

        self.assertIn('Turkey', result.data)

    def test_country_edit_valid(self):

        result = self.client.post(
            '/countries/edit/3',
            data={
                  'country_name': 'Turkey',
                  'country_abrev': 'TR'
            },
            follow_redirects=True
        )

        self.assertIn('<h1>Turkey</h1>', result.data)
        self.assertIn('<td>Turkey</td>', result.data)
        self.assertIn('<td>TR</td>', result.data)
        self.assertIn('<a href="/countries/edit/3">Edit</a>', result.data)
        self.assertIn('<a href="/countries/delete/3">Delete</a>', result.data)


    def test_country_edit_invalid(self):

        result = self.client.post(
            '/countries/edit/3',
            data={
                  'country_name': 'Turk8',
                  'country_abrev': ''
            },
            follow_redirects=True
        )

        self.assertIn('Please fill in a country name only with English letters.',
                       result.data)
        self.assertIn('Please fill in the country abbreviation with 2 characters.',
                       result.data)

    def test_country_form_validation(self):
        # ensure data is being cleansed, in ways we havent above
        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.client.post(
            '/countries/add',
            data={
                  'country_name': '',
                  'country_abrev': '98'
            },
            follow_redirects=True
        )
        # print result.data

        self.assertIn('Please fill in the country name',
                       result.data)
        self.assertIn('Please fill in the country abbreviation using only uppercase letters.',
                       result.data)



    def test_country_delete_valid(self):

        result = self.client.get(
            '/countries/delete/2',
            follow_redirects=True
        )
        # print result.data

        self.assertNotIn('France', result.data)

    def test_country_delete_invalid(self):

        result = self.client.get(
            '/countries/delete/10',
            follow_redirects=True
        )

        self.assertEqual(400, result.status_code)
        self.assertIn('Entry does not exist.', result.data)




if __name__ == '__main__':
    unittest.main()
