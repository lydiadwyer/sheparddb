from flask import Blueprint, render_template, redirect, url_for, current_app
from modules.Excavations.model import Excavation


# collection of URLs for the artifact section of the website
# setup the controller, use a local folder for templates
excavations = Blueprint(
    'excavations',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@excavations.route('/excavations')
def view_all_excavations():
    return render_template('excavations/view_all.html', Excavations=Excavation)

@excavations.route('/excavations/<excavation_id>')
def view_excavation(excavation_id):
    return render_template('excavations/view.html')  # , Artifacts=Artifact
