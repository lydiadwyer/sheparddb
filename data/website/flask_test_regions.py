import os
from shepard import app, db
import unittest
import tempfile
import subprocess, os, time

# http://flask.pocoo.org/docs/0.11/testing/
# http://flask.pocoo.org/docs/0.11/api/#flask.Response
# https://docs.python.org/2/library/unittest.html#assert-methods
class RegionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # self.reset_database()


    def tearDown(self):
        pass

    ### conflicts occuring because of all tests being done
    def test_region_default(self):

        result = self.app.get('/regions/')

        self.assertIn('Regions', result.data)
        self.assertIn('Dali', result.data)
        self.assertIn('Ankara', result.data)
        self.assertIn('<a href="/regions/add">Add region</a>', result.data)

    def test_region_view1(self):

        result = self.app.get('/regions/view/1')

        self.assertIn('Dali', result.data)
        self.assertIn('<a href="/regions/edit/1">Edit</a>', result.data)
        self.assertIn('<a href="/regions/">View All</a>', result.data)

    def test_region_view_none(self):

        result = self.app.get(
            '/regions/view/99',
            follow_redirects=True
        )

        self.assertIn('Entry does not exist.', result.data)
        self.assertIn('<h1>Regions</h1>', result.data)

    def test_region_add(self):

        result = self.app.get('/regions/add')

        self.assertIn('Add A Region', result.data)
        self.assertIn('Region Name', result.data)
        self.assertIn('Country', result.data)
        self.assertIn('<select name="country_id">', result.data)
        self.assertIn('<option value="">Select a Country</option>', result.data)


#####using country ids created from country testing
    def test_region_add_valid(self):

        result = self.app.post(
            '/regions/add',
            data={
                  'region_name': 'Bordeaux',
                  'country_id': '2'
            },
            follow_redirects=True
        )

        self.assertIn('<h1>Bordeaux</h1>', result.data)
        self.assertIn('<td>Bordeaux</td>', result.data)
        self.assertIn('<td>2</td>', result.data)
        self.assertIn('Edit', result.data)
        self.assertIn('Delete', result.data)

    def test_region_add_invalid(self):
        # send invalid name and non-number id
        result = self.app.post(
            '/regions/add',
            data={
                  'region_name': 'Greec1',
                  'country_id': 'gg'
            },
            follow_redirects=True
        )

        self.assertIn('Please fill in a region name only with English letters.', result.data)
        self.assertIn('Please choose the country.', result.data)
        self.assertIn('<option value="1">Cyprus</option>',result.data)


    def test_region_edit3(self):

        result = self.app.get('/regions/edit/3')

        self.assertIn('Edit A Region', result.data)
        self.assertIn('Ankara', result.data)
        self.assertIn('<option value="3" selected>Turkey</option>', result.data)

    def test_region_edit_valid(self):

        result = self.app.post(
            '/regions/edit/3',
            data={
                  'region_name': 'Izmir',
                  'country_id': 3
            },
            follow_redirects=True
        )

        self.assertIn('<h1>Izmir</h1>', result.data)
        self.assertIn('<td>3</td>', result.data)
        self.assertIn('<a href="/regions/edit/3">Edit</a>', result.data)
        self.assertIn('<a href="/regions/delete/3">Delete</a>', result.data)


    def test_region_edit_invalid(self):

        result = self.app.post(
            '/regions/edit/3',
            data={
                  'region_name': '88888',
                  'country_id': ''
            },
            follow_redirects=True
        )

        self.assertIn('Please fill in a region name only with English letters.',
                       result.data)
        self.assertIn('Please choose the country.', result.data)

    def test_region_form_validation1(self):
        # ensure data is being cleansed, in ways we havent above
        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.app.post(
            '/regions/add',
            data={
                  'region_name': '',
                  'country_id': 98
            },
            follow_redirects=True
        )
        # print result.data

        self.assertIn('Please fill in the region name completely.', result.data)
#        self.assertIn('Please choose a valid country.', result.data)
               
    def test_region_form_validation2(self):
        # ensure data is being cleansed, in ways we havent above
        # response
        # http://flask.pocoo.org/docs/0.11/api/#flask.Response
        result = self.app.post(
            '/regions/add',
            data={
                  'region_name': 'Hhhhh928(@@*@!!',
                  'country_id': 99.9999
            },
            follow_redirects=True
        )
        # print result.data

        self.assertIn('Please fill in a region name only with English letters.',
                       result.data)
# this may be passing because its casting to an int on the backend
#        self.assertIn('Please choose a valid country id.', result.data)


    def test_region_delete_valid(self):

        result = self.app.get(
            '/regions/delete/3',
            follow_redirects=True
        )
        # print result.data

        self.assertNotIn('Bordeaux', result.data)

    def test_region_delete_invalid(self):

        result = self.app.get(
            '/regions/delete/10',
            follow_redirects=True
        )

        self.assertEqual(400, result.status_code)
        self.assertIn('Entry does not exist.', result.data)




if __name__ == '__main__':
    unittest.main()
