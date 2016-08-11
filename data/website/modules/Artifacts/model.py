from modules.Shared.database import db
from sqlalchemy import Column, Integer, String, DateTime

# this part of the database that is the ARTIFACT TABLE
# http://flask-sqlalchemy.pocoo.org/2.1/models/
class Artifact(db.Model):

    __tablename__ = 'artifacts'

    """Artifact object model

    This is a Model class, used as a generic data container. It is an extension
    of the SQLAlchemy class, and inherits various common database actions.
    """

    artifact_id         = Column(Integer, primary_key=True)
    artifact_name       = Column(String(128), unique=True)
    artifact_created    = Column(DateTime)
    artifact_updated    = Column(DateTime)
    
        
    def __init__(self, artifact_name=""):
        self.artifact_name = artifact_name
        
    def __repr__(self):
        return "<Artifact(artifact_id='%s', artifact_name='%s', artifact_created='%s', artifact_updated='%s')>" % (
            self.artifact_id, self.artifact_name, self.artifact_created, self.artifact_updated)

        