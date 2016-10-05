"""
.. module:: database
    :platform: Unix
    :synopsis: Globally shared database connection
.. moduleauthor:: Lydia Dwyer
"""

from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine

# set up mongodb

db = SQLAlchemy()
mongo = MongoEngine()


"""
This is a shared database variable. It gets imported into all other Classes,
then initialized later with the Flask App.
"""
