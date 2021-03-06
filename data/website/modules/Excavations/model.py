#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Excavations Model class for the ShepardDB website."""

from modules.Shared.database import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


# this part of the database that is the EXCAVATIONS TABLE
# http://flask-sqlalchemy.pocoo.org/2.1/models/
class Excavation(db.Model):

    """Excavation object model

    This is a Model class, used as a generic data container. It is an extension
    of the SQLAlchemy class, and inherits various common database actions.
    """

    __tablename__ = 'excavations'


    excavation_id       = Column(Integer, primary_key=True)
    excavation_name     = Column(String(128), unique=True)
    country_id          = Column(Integer, ForeignKey('countries.country_id'))
    region_id           = Column(Integer, ForeignKey('regions.region_id'))
    city_id             = Column(Integer, ForeignKey('cities.city_id'))
    excavation_created  = Column(DateTime)
    excavation_updated  = Column(DateTime)

    def __init__(self, excavation_name=""):
        self.excavation_name = excavation_name

    def __repr__(self):
        return "<Excavation(excavation_id='%s', excavation_name='%s', excavation_created='%s',excavation_updated='%s')>" % (
            self.excavation_id, self.excavation_name, self.excavation_created, self.excavation_updated)
