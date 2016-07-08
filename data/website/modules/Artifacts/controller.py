from flask import Blueprint, render_template, redirect, url_for
from modules.Shared.database import db
from modules.Artifacts.model import Artifact



# setup the controller, use a local folder for templates
artifacts = Blueprint(
    'artifacts',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@artifacts.route('/artifacts')
def view_all_artifacts():
    return render_template('artifacts/view_all.html', Artifacts=Artifact)

@artifacts.route('/artifacts/<artifact_id>')
def view_artifact(artifact_id):
    return render_template('artifacts/view.html')  # , Artifacts=Artifact
