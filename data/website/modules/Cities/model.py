from modules.Shared.database import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

#this part of the database that is the CITIES TABLE
# http://flask-sqlalchemy.pocoo.org/2.1/models/
class City(db.Model):

    __tablename__ = 'cities'

    """City object model

    This is a Model class, used as a generic data container. It is an extension
    of the SQLAlchemy class, and inherits various common database actions.
    """

    city_id                = Column(Integer,
                                primary_key=True)
    city_name              = Column(String(128), unique=True)
    region_id              = Column(Integer, ForeignKey('regions.region_id'))
    country_id             = Column(Integer, ForeignKey('countries.country_id'))
#    country                = relationship("Country", back_populates="cities")
#    region                 = relationship("Region", back_populates="cities")
    child_excavations      = relationship("Excavation", backref="cities")
    
    def __init__(self, city_name=""):
        self.city_name    = city_name
        

