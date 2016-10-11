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
    This may be made a sub-document of Artifacts
    """
    
    
    #define ceramic attributes
    """ ceramic type is the type of ceramic onject,
         eg Vessel, Figurine, Industrial. String with limited options """
    ceramic_type = StringField(max_length=128, required=True)
    """ ceramic ware is the ware category eg. yellow buff ware.
        Strings with lots of options """ 
    ceramic_ware = StringField(max_length=128, required=True)
    """ ceramic form is the form of ceramic, such as cooking vessel
        or centaur-type figurine. String with lots of options """ 
    ceramic_form = StringField(max_length=128, required=True)
    """ ceramic registration id, the registration id of the ceramic object
        The ID is numeric or alphanumeric, and usually 
        unique within an excavation """ 
    ceramic_reg_id = IntField(max_length=128, required=True)
    """ date period is the archaeologically or historically defined era with
        a name and associated date range. This field is a string with limited
        options within a site, and sometimes but rarely changes """ 
    date_period = StringField(max_length=128, required=True)
    """ the site from which this was excavated. this field is for the offical
        whole site name, a String (often with non-english characters)
        this could be associated with the Excavation model """ 
    excavated_from = StringField(max_length=128, required=True)

    ## to do fields
    # parent fields: locus, pottery bucket, square, field, excavated_from
    # estimated dating/ terminus ante quem/post quem
    # ceramic fabric
    # decoration
    # other physical descriptors



