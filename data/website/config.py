
SQLALCHEMY_DATABASE_URI = 'postgresql://shepard:shepard@localhost/sheparddb'
SECRET_KEY = 'fda890t43nlba8i9pr32jl'


MONGODB_SETTINGS = {
        'db': 'sheparddb',
        'host': '127.0.0.1',
        'port': 27017                 
}

PORT = 9999
DEBUG_LOG_FILE = '/var/log/sheparddb/info.log'
WTF_CSRF_ENABLED = False
SQLALCHEMY_TRACK_MODIFICATIONS = True

