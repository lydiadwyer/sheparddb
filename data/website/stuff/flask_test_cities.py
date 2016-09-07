import subprocess, os, time
# from BaseTestCase import BaseTestCase
from flask_testing import TestCase
from flask import url_for

# http://flask.pocoo.org/docs/0.11/testing/
# http://flask.pocoo.org/docs/0.11/api/#flask.Response
# https://docs.python.org/2/library/unittest.html#assert-methods
class CityTestCase(TestCase):

    def reset_database(self):

        print 'CityTestCase::resetting...'

        conn = psycopg2.connect(
            "dbname=sheparddb user=shepard host=127.0.0.1 password=shepard")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(open("/vagrant/psql/db_create_schema.sql", "r").read())
        cursor.execute(open("/vagrant/psql/db_data.sql", "r").read())
        cursor.close()
        conn.close()

    def create_app(self):
        app = create_flask()
        app.config['TESTING'] = True
        app.testing = True
        # app = app.test_client()
        return app

    def setUp(self):
        # self.reset_database()
        self.app = self.create_app()

    def tearDown(self):
        pass

    # view all cities default
    def test_city_default(self):

        result = self.client.get(url_for('cities.view_all_cities'))

        self.assertIn('Cities', result.data)
        self.assertIn('Dali', result.data)
        self.assertIn('Tours', result.data)
        self.assertIn('<a href="/cities/add">Add city</a>', result.data)

    # view city number 1
    def test_city_view1(self):

        result = self.client.get('/cities/view/1')

        self.assertIn('Dali', result.data)
        self.assertIn('<a href="/cities/edit/1">Edit</a>', result.data)
        self.assertIn('<a href="/cities/">View All</a>', result.data)

    # try to view a city that does not exist
    def test_city_view_none(self):

        result = self.client.get(
            '/cities/view/99',
            follow_redirects=True
        )

        self.assertIn('Entry does not exist.', result.data)
        self.assertIn('<h1>Cities</h1>', result.data)

    # view the add page
    def test_city_add(self):

        result = self.client.get('/cities/add')

        self.assertIn('Add A City', result.data)
        self.assertIn('City Name', result.data)


#####using country ids created from country testing
    # test adding a city with valid outcome
    def test_city_add_valid(self):

        result = self.client.post(
            '/cities/add',
            data={
                  'city_name': 'Catal',
                  'country_id': '3',
                  'region_id': '3'
            },
            follow_redirects=True
        )

        self.assertIn('<h1>Catal</h1>', result.data)
        self.assertIn('<td>Catal</td>', result.data)
        self.assertIn('<td>3</td>', result.data)
        self.assertIn('Edit', result.data)
        self.assertIn('Delete', result.data)

    # test adding a city with invalid result
    def test_city_add_invalid(self):
        # send invalid name and non-number id
        result = self.client.post(
            '/cities/add',
            data={
                  'city_name': 'Greec1',
                  'country_id': 'gg',
                  'region_id': 'gg'
            },
            follow_redirects=True
        )

        self.assertIn('Please fill in a city name only with English letters.', result.data)
        self.assertIn('Please choose the country.', result.data)
        self.assertIn('Please choose the region.', result.data)
        self.assertIn('<option value="1">Cyprus</option>', result.data)

    # test editing a city page
    def test_city_edit3(self):

        result = self.client.get('/cities/edit/3')

        self.assertIn('Edit A City', result.data)
        self.assertIn('Istanbul', result.data)
        self.assertIn('<option value="3" selected>Turkey</option>', result.data)

    # test editing a city
    def test_city_edit_valid(self):

        result = self.client.post(
            '/cities/edit/3',
            data={
                  'city_name': 'Istabuli',
                  'country_id': 3,
                  'region_id': 3
            },
            follow_redirects=True
        )

        self.assertIn('<h1>Istabuli</h1>', result.data)
        self.assertIn('<a href="/cities/edit/3">Edit</a>', result.data)
        self.assertIn('<a href="/cities/delete/3">Delete</a>', result.data)

    # test invalid editing a city
    def test_city_edit_invalid(self):

        result = self.client.post(
            '/cities/edit/3',
            data={
                  'city_name': '88888',
                  'country_id': '',
                  'region_id': ''
            },
            follow_redirects=True
        )

        self.assertIn('Please fill in a city name only with English letters.',
                       result.data)
        self.assertIn('Please choose the country.', result.data)
        self.assertIn('Please choose the region.', result.data)

    # test that the city forms are validating data corretly
    def test_city_form_validation1(self):
        # ensure data is being cleansed, in ways we havent above
        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.client.post(
            '/cities/add',
            data={
                  'city_name': '',
                  'country_id': 9895,
                  'region_id': 9899
            },
            follow_redirects=True
        )
        # print result.data

        self.assertIn('Please fill in the city name completely.', result.data)
#        self.assertIn('Please choose a valid country.', result.data)

    def test_city_form_validation2(self):
        # ensure data is being cleansed, in ways we havent above
        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.client.post(
            '/cities/add',
            data={
                  'city_name': 'Hhhhh928(@@*@!!',
                  'country_id': 99.9999,
                  'region_id': 99.9999
            },
            follow_redirects=True
        )
        # print result.data

        self.assertIn('Please fill in a city name only with English letters.',
                       result.data)
# this may be passing because its casting to an int on the backend
#        self.assertIn('Please choose a valid country id.', result.data)

    # test that the cities are being deleted correctly
    def test_city_delete_valid(self):

        result = self.client.get(
            '/cities/delete/2',
            follow_redirects=True
        )
        # print result.data

        self.assertNotIn('Tours', result.data)

    # test that site responds correctly to invalid delete requests
    def test_city_delete_invalid(self):

        result = self.client.get(
            '/cities/delete/10',
            follow_redirects=True
        )

        self.assertEqual(400, result.status_code)
        self.assertIn('Entry does not exist.', result.data)


if __name__ == '__main__':
    unittest.main()
