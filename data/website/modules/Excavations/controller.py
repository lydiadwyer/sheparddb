#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Controller class for Excavations."""

import re
from flask import Blueprint, render_template, redirect, url_for, current_app, \
    request, abort
from modules.Excavations.model import Excavation
from modules.Cities.model import City
from modules.Regions.model import Region
from modules.Countries.model import Country
from modules.Shared.database import db

# collection of URLs for the excavations section of the website
# setup the controller, use a local folder for templates
excavations = Blueprint(
    'excavations',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/excavations'
)

@excavations.route('/')
def view_all_excavations():
    """ homepage with all excavations listed """
    return render_template('excavations/view_all.html', Excavations=Excavation)

@excavations.route('/view/<excavation_id>')
def view_one_excavation(excavation_id):
    entry = Excavation.query.get(excavation_id)
    return render_template('excavations/view.html', entry=entry)  

@excavations.route('/add', methods=['GET', 'POST'])
def add_excavation():
    """ add an excavation page function """
    
    entry = Excavation()  # creates a model.py instance, instance only has a name right now
    error_msg = {}
    form_is_valid = True
    country_list = Country.query.all()
    region_list = Region.query.all()
    city_list = City.query.all()

    if request.method == 'GET':
        return render_template('excavations/add.html', entry=entry, \
                               country_list=country_list, \
                               region_list=region_list, \
                               city_list=city_list, \
                               error_msg=error_msg)

    if request.method == 'POST':
        # validate input
        [entry, form_is_valid, error_msg] = form_validate_excavation(entry)

        # check if the form is valid
        if not form_is_valid:
            # current_app.logger.info('invalid add excavation')
            return render_template('excavations/add.html', entry=entry, \
                                   country_list=country_list, \
                                   region_list=region_list, \
                                   city_list=city_list, \
                                   error_msg=error_msg)
        #if data is valid, commit
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('excavations.view_one_excavation', \
                                excavation_id=entry.excavation_id))

@excavations.route('/edit/<excavation_id>', methods=['GET', 'POST'])
def edit_excavation(excavation_id):
    """ edit excavation details """

    # init variables
    entry = Excavation.query.get(excavation_id)
    error_msg = {}
    form_is_valid = True
    country_list = Country.query.all()
    region_list = Region.query.all()
    city_list = City.query.all()
    
    if request.method == 'GET':
        return render_template('excavations/edit.html', \
                               entry=entry, error_msg=error_msg, \
                               country_list=country_list, \
                               region_list=region_list, \
                               city_list=city_list)

    if request.method == 'POST':

        # validate input
        [entry, form_is_valid, error_msg] = form_validate_excavation(entry)

        # check if the form is valid
        if not form_is_valid:
            # current_app.logger.info('invalid edit excavation: ' + str(entry))
            return render_template('excavations/edit.html', entry=entry, \
                                   country_list=country_list, \
                                   region_list=region_list, \
                                   city_list=city_list, \
                                   error_msg=error_msg)

        # the data is valid, save it
        db.session.commit()
        return redirect(url_for('excavations.view_one_excavation', \
                                excavation_id=entry.excavation_id))
   # current_app.logger.error("unsupported method")


def form_validate_excavation(entry):
    """ validate Excavation form data """

    # retrieve data from the global Request object
    data = request.form

    # get string, cast to ASCII, truncate to 128 chars, strip multi spaces
    entry.excavation_name = \
        re.sub(' +', ' ',
               data['excavation_name'].encode('ascii', 'ignore')[:127])
    # retrieve ids in the data var from the html form
    entry.country_id = data['country_id']
    entry.region_id = data['region_id']
    entry.city_id = data['city_id']    
    
    # validate data
    form_is_valid = True
    error_msg = {}

    # ensure the excavation_name is filled in
    if not entry.excavation_name:
        form_is_valid = False
        error_msg['excavation_name'] = "Please fill in the excavation name."

    # excavation name underflow check, 1 or less characters
    if len(entry.excavation_name) < 2:
        form_is_valid = False
        error_msg['excavation_name'] = "Please fill in the excavation name completely."

    # ensure the excavation name is alphanumeric
    match = re.match('^[a-zA-Z0-9 ]*$', entry.excavation_name)
    if not match:
        form_is_valid = False
        error_msg['excavation_name'] = "Please fill in a excavation name only with English letters and numbers."
    else:
        current_app.logger.info("match = " + str(match.group(0)))
    
    # ensure country_id city_id region_id are chosen
    if not entry.country_id:
        form_is_valid = False
        error_msg['country_id'] = "Please choose the country."
    
    if not entry.region_id:
        form_is_valid = False
        error_msg['region_id'] = "Please choose the region."
        
    if not entry.city_id:
        form_is_valid = False
        error_msg['city_id'] = "Please choose the city."
        
    return [entry, form_is_valid, error_msg]


    
@excavations.route('/delete/<excavation_id>')
def delete_excavation(excavation_id):
    """ delete an excavation """
    entry = Excavation.query.get(Excavation_id)
    # check something doesnt exist
    if entry is None:
        return abort(400, 'Entry does not exist.')
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('excavations.view_all_excavations'))

