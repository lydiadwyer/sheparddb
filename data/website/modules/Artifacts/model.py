#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Artifacts Model class for the ShepardDB website."""

from modules.Shared.database import db
from sqlalchemy import Column, Integer, String, DateTime

# this part of the database that is the ARTIFACT TABLE
# http://flask-sqlalchemy.pocoo.org/2.1/models/

class Artifact(db.Model):

    """Artifact object model

    This is a Model class, used as a generic data container. It is an extension
    of the SQLAlchemy class, and inherits various common database actions.
    """

    __tablename__ = 'artifacts'

    artifact_id = Column(Integer, primary_key=True)
    artifact_name = Column(String(128))
    artifact_obj_reg = Column(Integer)
    artifact_created = Column(DateTime)
    artifact_updated = Column(DateTime)

    def __init__(self, artifact_name="", artifact_obj_reg=None):
        self.artifact_name = artifact_name
        self.artifact_obj_reg = artifact_obj_reg
