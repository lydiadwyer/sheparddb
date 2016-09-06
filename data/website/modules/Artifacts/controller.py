#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Controller class for Artifacts."""

from flask import Blueprint, render_template, redirect, url_for, \
    current_app, request
from modules.Artifacts.model import Artifact
from modules.Shared.database import db

# collection of URLs for the artifact section of the website
# setup the controller, use a local folder for templates
artifacts = Blueprint(
    'artifacts',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/artifacts'
)

#homepage with all artifacts in a table
@artifacts.route('/')
def view_all_artifacts():
    return render_template('artifacts/view_all.html', Artifacts=Artifact)

#view a single artifact in detail
@artifacts.route('/artifacts/view/<artifact_id>')
def view_artifact(artifact_id):
    
    # ensure that the artifact_id is numerica
    if not artifact_id.isdigit():
        current_app.logger.error("invalid artifact_id = " + artifact_id)
        return redirect(url_for("artifacts.view_all_artifacts"))
    
    # attempt to retrieve an Artifact using it's artifact_id
    entry = Artifact.query.get(artifact_id)
    
    # ensure we have a valid Artifact
    if None is entry:
        current_app.logger.error("invalid artifact_id = " + artifact_id + \
                                 ", entry = " + str(entry))
        return redirect(url_for("artifacts.view_all_artifacts"))
    
    # return the HTML page
    return render_template('artifacts/view.html', entry=entry)  # , Artifacts=Artifact

#add an artifact page function
@artifacts.route('/artifacts/add', methods = ['GET', 'POST'])
def add_artifact():
    
    if request.method == 'GET':
        return render_template('artifacts/add.html')  # , Artifacts=Artifact
    
    if request.method == 'POST':
        data = request.form
        entry = Artifact()  #creates a model.py instance, instance only has a name right now
        entry.artifact_name = str(data['artifact_name'])[:127] #set the Artifact name
        try:
            val = int(data['artifact_obj_reg'])
            if val > 1000000000:
                val = 1000000000
            entry.artifact_obj_reg = val
        except ValueError:
            entry.artifact_obj_reg = 0
        db.session.add(entry)
        db.session.commit()
        
        return redirect(url_for('artifacts.view_all_artifacts'))
    current_app.logger.error("unsupported method")
        
@artifacts.route('/artifacts/edit/<artifact_id>', methods = ['GET', 'POST'])
def edit_artifact(artifact_id):
    
    if request.method == 'GET':
        entry = Artifact.query.get(artifact_id)
        return render_template('artifacts/edit.html', entry=entry)  # , Artifacts=Artifact
    
    if request.method == 'POST':
        data = request.form
        entry = Artifact.query.get(artifact_id)
        entry.artifact_name = str(data['artifact_name'])[:127] #set the Artifact name
        try:
            val = int(data['artifact_obj_reg'])
            if val > 1000000000:
                val = 1000000000
            entry.artifact_obj_reg = val
        except ValueError:
            entry.artifact_obj_reg = 0
        db.session.commit()
        
        return redirect(url_for('artifacts.view_all_artifacts'))
    current_app.logger.error("unsupported method")

@artifacts.route('/artifacts/delete/<artifact_id>')
def delete_artifact(artifact_id):
    
    # ensure that the artifact_id is numerica
    if not artifact_id.isdigit():
        current_app.logger.error("invalid artifact_id = " + artifact_id)
        return redirect(url_for("artifacts.view_all_artifacts"))
    
    # attempt to retrieve the artifact
    entry = Artifact.query.get(artifact_id)
    
    # ensure we have a valid Artifact
    if None is entry:
        current_app.logger.error("invalid artifact_id = " + artifact_id + \
                                 ", entry = " + str(entry))
        return redirect(url_for("artifacts.view_all_artifacts"))
    
    # delete the artifact
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('artifacts.view_all_artifacts'))  # , Artifacts=Artifact
