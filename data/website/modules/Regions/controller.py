#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Controller class for Regions."""

import re
from flask import Blueprint, render_template, redirect, url_for, current_app, \
    request, abort
from modules.Regions.model import Region
from modules.Countries.model import Country
from modules.Shared.database import db

# collection of URLs for the artifact section of the website
# setup the controller, use a local folder for templates
regions = Blueprint(
    'regions',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/regions'
)

@regions.route('/')
def view_all_regions():
    """ homepage with all regions in a table """
    return render_template('regions/view_all.html', Regions=Region)

@regions.route('/view/<region_id>')
def view_one_region(region_id):
    """ view a single region in detail """
    entry = Region.query.get(region_id)
    return render_template('regions/view.html')

#########add country entry option for association
@regions.route('/add', methods=['GET', 'POST'])
def add_region():
    """ add an region page function """

    # init variables
    entry = Region()  # creates a model.py instance, instance only has a name right now
    error_msg = {}
    form_is_valid = True
    country_list = []
    ####need to query a list of all country ids + names and make list

    if request.method == 'GET':
        
        country_list = Country.query.all()
        return render_template('regions/add.html', entry=entry, \
                               country_id=country_list.country_id, \
                               country_name=country_list.country_name, \
                               error_msg=error_msg)

    if request.method == 'POST':
        # validate input
        [entry, form_is_valid, error_msg] = form_validate_region(entry)

        # check if the form is valid
        if not form_is_valid:
            # current_app.logger.info('invalid add region')
            return render_template('regions/add.html', entry=entry, \
                                   error_msg=error_msg)

        # the data is valid, save it
        db.session.add(entry)
        db.session.commit()

        return redirect(url_for('regions.view_region', \
                                region_id=entry.region_id))
    # current_app.logger.error("unsupported method")

#### should add country entry option
@regions.route('/edit/<region_id>')
def edit_region(region_id):
    """ edit region details """

    # init variables
    entry = Region.query.get(region_id)
    error_msg = {}
    form_is_valid = True

    ##### should I be using url_for here or hardcoding?
    if request.method == 'GET':
        return render_template(url_for('regions.edit_region', \
                               region_id=entry.region_id))

    if request.method == 'POST':

        # validate input
        [entry, form_is_valid, error_msg] = form_validate_region(entry)

        # check if the form is valid
        if not form_is_valid:
            # current_app.logger.info('invalid edit region: ' + str(entry))
            return render_template('regions/edit.html', entry=entry, \
                                   error_msg=error_msg)

        # the data is valid, save it
        db.session.commit()
        return redirect(url_for('regions.view_region', \
                                region_id=entry.region_id))
   # current_app.logger.error("unsupported method")

def form_validate_region(entry):
    """ validate Region form data """

    # retrieve data from the global Request object
    data = request.form

    # get string, cast to ASCII, truncate to 128 chars, strip multi spaces
    entry.region_name = \
        re.sub(' +', ' ',
               data['region_name'].encode('ascii', 'ignore')[:127])

    # validate data
    form_is_valid = True
    error_msg = {}

    # ensure the region_name is filled in
    if not entry.region_name:
        form_is_valid = False
        error_msg['region_name'] = "Please fill in the region name."

    # region name underflow check
    if len(entry.region_name) < 4:
        form_is_valid = False
        error_msg['region_name'] = "Please fill in the region name completely."

    # ensure the region name is letters
    match = re.match('^[a-zA-Z ]*$', entry.region_name)
    if not match:
        form_is_valid = False
        error_msg['region_name'] = "Please fill in a region name only with English letters."
    else:
        current_app.logger.info("match = " + str(match.group(0)))

    return [entry, form_is_valid, error_msg]


@regions.route('/delete/<region_id>')
def delete_region(region_id):
    """ delete a region """
    entry = Region.query.get(region_id)
    # check something doesnt exist
    if entry is None:
        return abort(400, 'Entry does not exist.')
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('regions.view_all_regions'))

