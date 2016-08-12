from flask import Blueprint, render_template, redirect, url_for, current_app, request
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

#homepage with all countries in a table
@countries.route('/countries')
def view_all_countries():
    return render_template('countries/view_all.html', Countries=Country)

#view a single country in detail
@countries.route('/countries/view/<country_id>')
def view_country(country_id):
    entry = Country.query.get(country_id)
    return render_template('countries/view.html', entry=entry)  # , Countries=Country

####restrict who can add/edit/delete countries?
#add an country page function
@countries.route('/countries/add', methods = ['GET', 'POST'])
def add_country():
    
    if request.method == 'GET':
        return render_template('countries/add.html')  # , Countries=Country
    
    if request.method == 'POST':
        data = request.form
        entry = Country()  #creates a model.py instance, instance only has a name right now
        entry.country_name = str(data['country_name'])[:127] #set the Country name
        entry.country_abrev = str(data['country_abrev'])[:127]
        db.session.add(entry)
        db.session.commit()
        
        return redirect(url_for('countries.view_all_countries'))
    current_app.logger.error("unsupported method")
        
@countries.route('/countries/edit/<country_id>', methods = ['GET', 'POST'])
def edit_country(country_id):
    
    if request.method == 'GET':
        entry = Country.query.get(country_id)
        return render_template('countries/edit.html', entry=entry)  # , Countries=Country
    
    if request.method == 'POST':
        data = request.form
        entry = Country.query.get(country_id)
        entry.country_name = str(data['country_name'])[:127] #set the Country name
        entry.country_abrev = str(data['country_abrev'])[:127]
        db.session.commit()
        
        return redirect(url_for('countries.view_all_countries'))
    current_app.logger.error("unsupported method")

@countries.route('/countries/delete/<country_id>')
def delete_country(country_id):
    entry = Country.query.get(country_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('countries.view_all_countries'))  # , Countries=Country
