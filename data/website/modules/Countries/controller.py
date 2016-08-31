#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Controller class for Countries."""

import re
from flask import Blueprint, render_template, redirect, url_for, current_app, \
    request, abort, flash, jsonify
from modules.Countries.model import Country
from modules.Shared.database import db

# collection of URLs for the COUNTRY section of the website
# setup the controller, use a local folder for templates
countries = Blueprint(
    'countries',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/countries'
)

@countries.route('/')
def view_all_countries():
    """ homepage with all countries in a table """
    return render_template('countries/view_all.html', Countries=Country)


@countries.route('/view/<country_id>')
def view_country(country_id):
    """ view a single country in detail """
    # validate view to return view_country page if country_id exists,
    # else return to view all
    entry = Country.query.get(country_id)
    if not entry is None:
        return render_template('countries/view.html', entry=entry)
    else:
        flash('Entry does not exist.', 'error')
        return redirect(url_for('countries.view_all_countries'))

@countries.route('/add', methods=['GET', 'POST'])
def add_country():
    """ add an country page function """


    # init variables
    entry = Country()  # creates a model.py instance, instance only has a name right now
    error_msg = {}
    form_is_valid = True

    if request.method == 'GET':
        return render_template('countries/add.html', entry=entry, \
                               error_msg=error_msg)

    if request.method == 'POST':
        # validate input
        [entry, form_is_valid, error_msg] = form_validate_country(entry)

        # check if the form is valid
        if not form_is_valid:
            # check if it gets an ajax request
            if request.is_xhr:
                return jsonify({ 'error_msg': error_msg})
            # current_app.logger.info('invalid add country')
            return render_template('countries/add.html', entry=entry, \
                                   error_msg=error_msg)

        # the data is valid, save it
        db.session.add(entry)
        db.session.commit()

        return redirect(url_for('countries.view_country', \
                                country_id=entry.country_id))
    # current_app.logger.error("unsupported method")

@countries.route('/edit/<country_id>', methods=['GET', 'POST'])
def edit_country(country_id):
    """ edit country details """

    # init variables
    entry = Country.query.get(country_id)
    error_msg = {}
    form_is_valid = True

    if request.method == 'GET':
        return render_template('countries/edit.html', \
                               entry=entry, error_msg=error_msg)

    if request.method == 'POST':

        # validate input
        [entry, form_is_valid, error_msg] = form_validate_country(entry)

        # check if the form is valid
        if not form_is_valid:
            # current_app.logger.info('invalid edit country: ' + str(entry))
            return render_template('countries/edit.html', entry=entry, \
                                   error_msg=error_msg)

        # the data is valid, save it
        db.session.commit()
        return redirect(url_for('countries.view_country', \
                                country_id=entry.country_id))
   # current_app.logger.error("unsupported method")

def form_validate_country(entry):
    """ validate Country form data """
    # validate data vars
    form_is_valid = True
    error_msg = {}
    # retrieve data from the global Request object
    data = request.form
    
    if not 'country_name' in data \
        or not 'country_abrev' in data:
    
        if not 'country_name' in data:
            error_msg['country_name'] = "Please fill in the country name."
        if not 'country_abrev' in data:
            error_msg['country_abrev'] = "Please fill in the country abbreviation."
        form_is_valid = False
        return [entry, form_is_valid, error_msg]

    # get string, cast to ASCII, truncate to 32 chars, strip multi spaces
    entry.country_name = \
        re.sub(' +', ' ',
               data['country_name'].encode('ascii', 'ignore')[:32])

    # get string, cast to ASCII, truncate to 3 chars, strip multi spaces
    entry.country_abrev = \
        re.sub(' +', ' ',
               data['country_abrev'].encode('ascii', 'ignore')[:2])


    # ensure the country_name is filled in
    if not entry.country_name:
        form_is_valid = False
        error_msg['country_name'] = "Please fill in the country name."

    # country name underflow check
    if len(entry.country_name) < 4:
        form_is_valid = False
        error_msg['country_name'] = "Please fill in the country name completely."

    # ensure the country name is letters
    match = re.match('^[a-zA-Z ]*$', entry.country_name)
    if not match:
        form_is_valid = False
        error_msg['country_name'] = "Please fill in a country name only with English letters."
    else:
        current_app.logger.info("match = " + str(match.group(0)))

    # ensure the country abbrev is filled in
    if not entry.country_abrev:
        form_is_valid = False
        error_msg['country_abrev'] = "Please fill in the country abbreviation."

    # ensure the abbrev is 2 characters
    if len(entry.country_abrev) != 2:
        form_is_valid = False
        error_msg['country_abrev'] = "Please fill in the country abbreviation with 2 characters."

    # ensure the abbrev is uppercase letters
    match = re.match('^[A-Z ]*$', entry.country_abrev)
    if not match:
        form_is_valid = False
        error_msg['country_abrev'] = \
            "Please fill in the country abbreviation using only uppercase letters."
    else:
        current_app.logger.info("match = " + str(match.group(0)))

    return [entry, form_is_valid, error_msg]

@countries.route('/delete/<country_id>')
def delete_country(country_id):
    """ delete a country """
    entry = Country.query.get(country_id)
    # check something doesnt exist
    if entry is None:
        return abort(400, 'Entry does not exist.')
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('countries.view_all_countries'))
