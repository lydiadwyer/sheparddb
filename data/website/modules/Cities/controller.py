from flask import Blueprint, render_template, redirect, url_for, current_app
from modules.Cities.model import City


# collection of URLs for the artifact section of the website
# setup the controller, use a local folder for templates
cities = Blueprint(
    'cities',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@cities.route('/')
def view_all_cities():
    return render_template('cities/view_all.html', Cities=City)

@cities.route('/view/<city_id>')
def view_city(city_id):
    return render_template('cities/view.html')  
