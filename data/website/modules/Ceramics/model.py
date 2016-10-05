#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Ceramics Model class for the ShepardDB website, Mongo Database."""

from modules.Shared.database import mongo
from mongoengine import Document
from mongoengine import StringField, IntField

# this part of the mongo database that is the CERAMIC TABLE
# http://flask-appbuilder.readthedocs.io/en/latest/quickhowto_mongo.html
#### look at document inheritance for maybe handling artifacts
# http://docs.mongoengine.org/guide/defining-documents.html#document-inheritance


class Ceramic(mongo.Document):

    """Ceramic object model

    This is a Document class, used as a generic data container. It is an extension
    of the MongoEngine class, and inherits various common database actions.
    """
    #define ceramic attributes
    ceramic_type = StringField(max_length=128, required=True)
    ceramic_ware = StringField(max_length=128, required=True)
    ceramic_form = StringField(max_length=128, required=True)
    ceramic_reg_id = IntField(max_length=128, required=True)
    # get time period ceramic dated to
    date_period = StringField(max_length=128)
    excavated_from = StringField(max_length=128, required=True)
    

