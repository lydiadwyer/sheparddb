from modules.Shared.database import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

# this part of the database that is the REGIONS TABLE
# http://flask-sqlalchemy.pocoo.org/2.1/models/
class Region(db.Model):

    __tablename__ = 'regions'

    """Region object model

    This is a Model class, used as a generic data container. It is an extension
    of the SQLAlchemy class, and inherits various common database actions.
    """

    region_id = Column(Integer,
                                primary_key=True)
    region_name = Column(String(128), unique=True)
    country_id = Column(Integer, ForeignKey('countries.country_id'))
    cities = relationship("City", cascade="delete, delete-orphan")

    def __init__(self, region_name=""):
        self.region_name = region_name

