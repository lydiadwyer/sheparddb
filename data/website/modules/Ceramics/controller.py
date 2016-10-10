#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Controller class for Ceramics."""

from flask import Blueprint, render_template, redirect, url_for, \
    current_app, request
from flask_mongoengine import MongoEngine
from modules.Ceramics.model import Ceramic
from modules.Shared.database import mongo


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



  
#view a single ceramic artifact in detail
@ceramics.route('/view/<id>')
def view_ceramic(id):
     
    entry = Ceramic.objects.get(id=id)
      
    # ensure we have a valid ceramic object
    if None is entry:
        current_app.logger.error("invalid id = " + id + \
                                 ", entry = " + str(entry))
        return redirect(url_for("ceramics.view_all_ceramics"))
      
    # return the HTML page
    return render_template('ceramics/view.html', entry=entry)  # , Artifacts=Artifact
  
 
 
#add a ceramic page function
@ceramics.route('/add', methods = ['GET', 'POST'])
def add_ceramic():
     
    if request.method == 'GET':
        return render_template('ceramics/add.html')  
     
    if request.method == 'POST':
        data = request.form.to_dict()
        entry = Ceramic(**data).save()
         
        return redirect(url_for('ceramics.view_all_ceramics'))
    current_app.logger.error("unsupported method")
    
    
 
@ceramics.route('/edit/<id>', methods = ['GET', 'POST'])
def edit_ceramic(id):
      
    if request.method == 'GET':
        entry = Ceramic.objects.get(id=id)
        return render_template('ceramics/edit.html', entry=entry)  # , Artifacts=Artifact
      
    if request.method == 'POST':
        data = request.form.to_dict()

        
        Ceramic.objects(id=id).update(**data)

        return redirect(url_for('ceramics.view_all_ceramics'))
    current_app.logger.error("unsupported method")
  
@ceramics.route('/delete/<id>')
def delete_ceramic(id):
      
      
    # attempt to retrieve the ceramic object
    entry = Ceramic.objects.get(id=id)
      
    # ensure we have a valid Artifact
    if None is entry:
        current_app.logger.error("invalid id = " + id + \
                                 ", entry = " + str(entry))
        return redirect(url_for("ceramics.view_all_ceramics"))
      
    # delete the artifact
    
    Ceramic.objects(id=entry.id).delete()
    
    
    return redirect(url_for('ceramics.view_all_ceramics'))  # , Artifacts=Artifact
