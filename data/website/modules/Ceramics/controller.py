#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Controller class for Ceramics."""

from flask import Blueprint, render_template, redirect, url_for, \
    current_app, request
from modules.Ceramics.model import Ceramic
from modules.Shared.database import db, mongo

# collection of URLs for the ceramics section of the website
# setup the controller, use a local folder for templates
ceramics = Blueprint(
    'ceramics',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/ceramics'
)

#homepage with all ceramics in a table
@ceramics.route('/')
def view_all_ceramics():
    return render_template('ceramics/view_all.html', Ceramics=Ceramic)
#===============================================================================
# 
# #view a single artifact in detail
# @ceramics.route('/ceramics/view/<artifact_id>')
# def view_artifact(artifact_id):
#     
#     # ensure that the artifact_id is numerica
#     if not artifact_id.isdigit():
#         current_app.logger.error("invalid artifact_id = " + artifact_id)
#         return redirect(url_for("ceramics.view_all_ceramics"))
#     
#     # attempt to retrieve an Artifact using it's artifact_id
#     entry = Artifact.query.get(artifact_id)
#     
#     # ensure we have a valid Artifact
#     if None is entry:
#         current_app.logger.error("invalid artifact_id = " + artifact_id + \
#                                  ", entry = " + str(entry))
#         return redirect(url_for("ceramics.view_all_ceramics"))
#     
#     # return the HTML page
#     return render_template('ceramics/view.html', entry=entry)  # , Artifacts=Artifact
# 
# #add an artifact page function
# @ceramics.route('/ceramics/add', methods = ['GET', 'POST'])
# def add_artifact():
#     
#     if request.method == 'GET':
#         return render_template('ceramics/add.html')  # , Artifacts=Artifact
#     
#     if request.method == 'POST':
#         data = request.form
#         entry = Artifact()  #creates a model.py instance, instance only has a name right now
#         entry.artifact_name = str(data['artifact_name'])[:127] #set the Artifact name
#         try:
#             val = int(data['artifact_obj_reg'])
#             if val > 1000000000:
#                 val = 1000000000
#             entry.artifact_obj_reg = val
#         except ValueError:
#             entry.artifact_obj_reg = 0
#         db.session.add(entry)
#         db.session.commit()
#         
#         return redirect(url_for('ceramics.view_all_ceramics'))
#     current_app.logger.error("unsupported method")
#         
# @ceramics.route('/ceramics/edit/<artifact_id>', methods = ['GET', 'POST'])
# def edit_artifact(artifact_id):
#     
#     if request.method == 'GET':
#         entry = Artifact.query.get(artifact_id)
#         return render_template('ceramics/edit.html', entry=entry)  # , Artifacts=Artifact
#     
#     if request.method == 'POST':
#         data = request.form
#         entry = Artifact.query.get(artifact_id)
#         entry.artifact_name = str(data['artifact_name'])[:127] #set the Artifact name
#         try:
#             val = int(data['artifact_obj_reg'])
#             if val > 1000000000:
#                 val = 1000000000
#             entry.artifact_obj_reg = val
#         except ValueError:
#             entry.artifact_obj_reg = 0
#         db.session.commit()
#         
#         return redirect(url_for('ceramics.view_all_ceramics'))
#     current_app.logger.error("unsupported method")
# 
# @ceramics.route('/ceramics/delete/<artifact_id>')
# def delete_artifact(artifact_id):
#     
#     # ensure that the artifact_id is numerica
#     if not artifact_id.isdigit():
#         current_app.logger.error("invalid artifact_id = " + artifact_id)
#         return redirect(url_for("ceramics.view_all_ceramics"))
#     
#     # attempt to retrieve the artifact
#     entry = Artifact.query.get(artifact_id)
#     
#     # ensure we have a valid Artifact
#     if None is entry:
#         current_app.logger.error("invalid artifact_id = " + artifact_id + \
#                                  ", entry = " + str(entry))
#         return redirect(url_for("ceramics.view_all_ceramics"))
#     
#     # delete the artifact
#     db.session.delete(entry)
#     db.session.commit()
#     return redirect(url_for('ceramics.view_all_ceramics'))  # , Artifacts=Artifact
#===============================================================================
