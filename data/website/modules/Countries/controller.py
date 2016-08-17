#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Controller class for Countries."""

from flask import Blueprint, render_template, redirect, url_for, current_app, \
    request
from modules.Countries.model import Country
from modules.Shared.database import db

# collection of URLs for the artifact section of the website
# setup the controller, use a local folder for templates
countries = Blueprint(
    'countries',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@countries.route('/countries')
def view_all_countries():
    """ homepage with all countries in a table """
    return render_template('countries/view_all.html', Countries=Country)


@countries.route('/countries/view/<country_id>')
def view_country(country_id):
    """ view a single country in detail """
    entry = Country.query.get(country_id)
    return render_template('countries/view.html', entry=entry)

####restrict who can add/edit/delete countries?
@countries.route('/countries/add', methods=['GET', 'POST'])
def add_country():
    """ add an country page function """

    # create a blank Country instance
    entry = Country()  # creates a model.py instance, instance only has a name right now
    error_msg = {}

    if request.method == 'GET':
        return render_template('countries/add.html', entry=entry, \
                               error_msg=error_msg)

    if request.method == 'POST':
        data = request.form
        entry.country_name = str(data['country_name'])[:32]
        entry.country_abrev = str(data['country_abrev'])[:3]

        # validate data
        form_is_valid = True

        # ensure the country_name is filled in
        if not entry.country_name:
            form_is_valid = False
            error_msg['country_name'] = "Please fill in the country name"

        # ensure the country_name is filled in
        if not entry.country_abrev:
            form_is_valid = False
            error_msg['country_abrev'] = "Please fill in the country abbreviation"



        # check if the form is valid
        if not form_is_valid:
            current_app.logger.info('invalid add country')
            return render_template('countries/add.html', entry=entry, \
                                   error_msg=error_msg)

        # the data is valid, save it
        db.session.add(entry)
        db.session.commit()

        return redirect(url_for('countries.view_country', \
                                country_id=entry.country_id))
    current_app.logger.error("unsupported method")

@countries.route('/countries/edit/<country_id>', methods=['GET', 'POST'])
def edit_country(country_id):
    """ edit country details """
    if request.method == 'GET':
        entry = Country.query.get(country_id)
        return render_template('countries/edit.html', entry=entry)

    if request.method == 'POST':
        data = request.form
        entry = Country.query.get(country_id)
        entry.country_name = str(data['country_name'])[:127]
        entry.country_abrev = str(data['country_abrev'])[:127]
        db.session.commit()

        return redirect(url_for('countries.view_country', \
                                country_id=entry.country_id))
    current_app.logger.error("unsupported method")

@countries.route('/countries/delete/<country_id>')
def delete_country(country_id):
    """ delete a country """
    entry = Country.query.get(country_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('countries.view_all_countries'))
