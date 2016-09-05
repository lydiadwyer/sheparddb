#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Controller class for Cities."""

import re
from flask import Blueprint, render_template, redirect, url_for, current_app, \
    request, abort
from modules.Cities.model import City
from modules.Regions.model import Region
from modules.Countries.model import Country
from modules.Shared.database import db

# collection of URLs for the cities section of the website
# setup the controller, use a local folder for templates
cities = Blueprint(
    'cities',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/cities'
)  


@cities.route('/')
def view_all_cities():
    """ homepage with all cities in a table """
    
    return render_template('cities/view_all.html', Cities=City)

@cities.route('/view/<city_id>')
def view_one_city(city_id):
    """ view a single city in detail """
    entry = City.query.get(city_id)
    if not entry is None:
        return render_template('cities/view.html', entry=entry)
    else:
        flash('Entry does not exist.', 'error')
        return redirect(url_for('cities.view_all_cities'))

@cities.route('/add', methods=['GET', 'POST'])
def add_city():
    """ add a city page function """

    # init variables
    entry = City()  # creates a model.py instance, instance only has a name right now
    error_msg = {}
    form_is_valid = True
    country_list = Country.query.all()
    region_list = Region.query.all()

    if request.method == 'GET':
        return render_template('cities/add.html', entry=entry, \
                               country_list=country_list, \
                               region_list=region_list, \
                               error_msg=error_msg)

    if request.method == 'POST':
        # validate input
        [entry, form_is_valid, error_msg] = form_validate_city(entry)

        # check if the form is valid
        if not form_is_valid:
            # current_app.logger.info('invalid add city')
            return render_template('cities/add.html', entry=entry, \
                                   country_list=country_list, \
                                   region_list=region_list, \
                                   error_msg=error_msg)

        # the data is valid, save it
        db.session.add(entry)
        db.session.commit()

        return redirect(url_for('cities.view_one_city', \
                                city_id=entry.city_id))
    # current_app.logger.error("unsupported method")


@cities.route('/edit/<city_id>', methods=['GET', 'POST'])
def edit_city(city_id):
    """ edit city details """

    # init variables
    entry = City.query.get(city_id)
    error_msg = {}
    form_is_valid = True
    country_list = Country.query.all()
    region_list = Region.query.all()

    if request.method == 'GET':
        return render_template('cities/edit.html', \
                               entry=entry, error_msg=error_msg, \
                               country_list=country_list, \
                               region_list=region_list)

    if request.method == 'POST':

        # validate input
        [entry, form_is_valid, error_msg] = form_validate_city(entry)

        # check if the form is valid
        if not form_is_valid:
            # current_app.logger.info('invalid edit city: ' + str(entry))
            return render_template('cities/edit.html', entry=entry, \
                                   country_list=country_list, \
                                   region_list=region_list, \
                                   error_msg=error_msg)

        # the data is valid, save it
        db.session.commit()
        return redirect(url_for('cities.view_one_city', \
                                city_id=entry.city_id))
   # current_app.logger.error("unsupported method")

def form_validate_city(entry):
    """ validate City form data """
    # validate data
    form_is_valid = True
    error_msg = {}
    # retrieve data from the global Request object
    data = request.form
    if not fields['city_name', 'country_id', 'region_id'] in data:
        
        if not 'city_name' in data:
            error_msg['city_name'] = "Please fill in the city name."
        if not 'country_id' in data:
            error_msg['country_id'] = "Please choose the country."
        if not 'region_id' in data:
            error_msg['region_id'] = "Please choose the region."
        form_is_valid = False
        return [entry, form_is_valid, error_msg]
    # get string, cast to ASCII, truncate to 128 chars, strip multi spaces
    entry.city_name = \
        re.sub(' +', ' ',
               data['city_name'].encode('ascii', 'ignore')[:127])

    # retrieve ids in the data var from the html form
    if data['country_id'].isdigit():
        entry.country_id = int(data['country_id'])
    else:
        form_is_valid=False
        error_msg['country_id'] = "Please choose the country."
    
    if data['region_id'].isdigit():
        entry.region_id = int(data['region_id'])
    else:
        form_is_valid=False
        error_msg['region_id'] = "Please choose the region."

    # ensure the city_name is filled in
    if not entry.city_name:
        form_is_valid = False
        error_msg['city_name'] = "Please fill in the city name."

    # city name underflow check, 2 or less characters
    if len(entry.city_name) < 3:
        form_is_valid = False
        error_msg['city_name'] = "Please fill in the city name completely."

    # ensure the city name is letters
    match = re.match('^[a-zA-Z ]*$', entry.city_name)
    if not match:
        form_is_valid = False
        error_msg['city_name'] = "Please fill in a city name only with English letters."
    else:
        current_app.logger.info("match = " + str(match.group(0)))
    
    # ensure country_id and region_id are chosen
    if not entry.country_id:
        form_is_valid = False
        error_msg['country_id'] = "Please choose the country."
    
    if not entry.region_id:
        form_is_valid = False
        error_msg['region_id'] = "Please choose the region."

    return [entry, form_is_valid, error_msg]


@cities.route('/delete/<city_id>')
def delete_city(city_id):
    """ delete a city """
    entry = City.query.get(city_id)
    # check something doesnt exist
    if entry is None:
        return abort(400, 'Entry does not exist.')
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('cities.view_all_cities'))