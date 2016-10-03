"""
.. module:: database
    :platform: Unix
    :synopsis: Globally shared database connection
.. moduleauthor:: Lydia Dwyer + Apollo Clark <apolloclark@gmail.com>
"""

from flask_sqlalchemy import SQLAlchemy

# connect to mongo db

db = SQLAlchemy()



"""
This is a shared database variable. It gets imported into all other Classes,
then initialized later with the Flask App.
"""
