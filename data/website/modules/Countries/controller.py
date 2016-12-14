#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Controller class for Countries."""

import re
from flask import Blueprint, render_template, redirect, url_for, current_app, \
    request, abort, flash, jsonify, make_response
from psycopg2 import IntegrityError
from sqlalchemy import exc
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

@countries.route('/', methods=['GET'])
def view_all_countries():
    """ homepage with all countries in a table """
    
    # serialize all the Country database entries into an array of dicts
    Countries = []
    for entry in Country.query.order_by('country_id').all():
        Countries.append(entry.serialize())
    
    return jsonify(Countries)
    #return render_template('countries/view_all.html', Countries=Country)


@countries.route('/<country_id>', methods=['GET'])
def view_country(country_id):
    """ view a single country in detail """
    # validate view to return view_country page if country_id exists,
    # else return to view all
    entry = Country.query.get(country_id)
    if not entry is None:
        return jsonify(entry.serialize())
        #return render_template('countries/view.html', entry=entry)
    else:
        abort(500, "Entry does not exist")

@countries.route('/', methods=['POST'])
def add_country():
    """ add a country function """

    #make an entry to insert
    entry = Country()  
    error_msg = {}
    form_is_valid = True

    # validate input
    # the form_validate is actually grabbing the incoming request data
    [entry, form_is_valid, error_msg] = form_validate_country(entry)

    # check if the form is valid
    if not form_is_valid:
        abort(make_response(jsonify({'error_msg': error_msg}), 400))

    # if the data is valid, try to save it
    # else throw an error
    try:
        db.session.add(entry)
        db.session.commit()
    except exc.SQLAlchemyError:
        db.session.rollback()
        db.session.flush()
        abort(make_response(
            jsonify({'error_msg': "You tried to add something that already exists"}), 400))
        
    
    return jsonify(entry.serialize())

@countries.route('/<country_id>', methods=['PUT'])
def edit_country(country_id):
    """ edit country details """

    # init variables
    entry = Country.query.get(country_id)
    error_msg = {}
    form_is_valid = True

    # validate input
    # the form_validate function is where the request data is being grabbed
    [entry, form_is_valid, error_msg] = form_validate_country(entry)

    # check if the form is valid
    if not form_is_valid:
        abort(make_response(jsonify({'error_msg': error_msg}), 400))

    # if the data is valid, try to save it
    # else throw an error
    try:
        db.session.commit()
    except exc.SQLAlchemyError:
        db.session.rollback()
        db.session.flush()
        abort(make_response(
            jsonify({'error_msg': "The edit contained something that already exists"}), 400))
        
    
    return jsonify(entry.serialize())
   # current_app.logger.error("unsupported method")

@countries.route('/<country_id>', methods=['DELETE'])
def delete_country(country_id):
    """ delete a country """
    entry = Country.query.get(country_id)
    # check something doesnt exist
    if entry is None:
        return abort(400, 'Entry does not exist.')
    
    try:
        db.session.delete(entry)
        db.session.commit()
    except exc.SQLAlchemyError:
        db.session.rollback()
        db.session.flush()
        abort(make_response(
            jsonify({'error_msg': "The delete went wrong"}), 400))
        
    
    return view_all_countries()


def form_validate_country(entry):
    """ validate Country form data """
    # validate data vars
    form_is_valid = True
    error_msg = {}
    # retrieve data from the global Request object
    data = request.get_json()
    
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

