from flask import Blueprint, render_template, redirect, url_for, current_app
from modules.Regions.model import Region


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
    return render_template('regions/view_all.html', Regions=Region)

@regions.route('/view/<region_id>')
def view_one_region(region_id):
    return render_template('regions/view.html')

@regions.route('/edit/<region_id>')
def edit_region(region_id):
    return render_template('regions/view.html')


@regions.route('/delete/<region_id>')
def delete_region(region_id):
    return render_template('regions/view.html')

