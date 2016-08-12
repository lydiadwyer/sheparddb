from modules.Shared.database import db
from sqlalchemy import Column, Integer, String, DateTime

# this part of the database that is the ARTIFACT TABLE
# http://flask-sqlalchemy.pocoo.org/2.1/models/
class Country(db.Model):

    __tablename__ = 'countries'

    """Country object model

    This is a Model class, used as a generic data container. It is an extension
    of the SQLAlchemy class, and inherits various common database actions.
    """

    country_id         = Column(Integer, primary_key=True)
    country_name       = Column(String(128), unique=True)
    country_abrev      = Column(String(128), unique=True)
    country_created    = Column(DateTime)
    #do I even need country created?
        
    def __init__(self, country_name="", country_abrev=""):
        self.country_name    = country_name
        self.country_abrev   = country_abrev
        
    def __repr__(self):
        return "<Country(country_id='%s', country_name='%s', country_abrev='%s', country_created='%s')>" % (
            self.country_id, self.country_name, self.country_abrev, self.country_created)

        