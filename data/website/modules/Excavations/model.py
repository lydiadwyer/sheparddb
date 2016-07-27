from modules.Shared.database import db
from sqlalchemy import Column, Integer, String, DateTime

#this part of the database that is the ARTIFACT TABLE
# http://flask-sqlalchemy.pocoo.org/2.1/models/
class Excavation(db.Model):

    __tablename__ = 'excavations'

    """Excavation object model

    This is a Model class, used as a generic data container. It is an extension
    of the SQLAlchemy class, and inherits various common database actions.
    """

    excavation_id = Column(Integer, primary_key=True)
    excavation_name = Column(String(128), unique=True)
    excavation_created = Column(DateTime)
    excavation_updated = Column(DateTime)
