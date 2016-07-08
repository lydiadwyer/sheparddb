#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

# import various routes
from modules.Shared.database import db
from modules.Artifacts.controller import artifacts




# create app
app = Flask(__name__)

# configure settings
app.config.from_pyfile('config.py')

# setup database handler
db.init_app(app)

# register the module controllers
app.register_blueprint(artifacts)




# example of a simple static route
@app.route('/')
def home():
    return render_template('home.html')

# example of a simple static route, with a unique name
@app.route('/test')
def test():
    return 'this is not a test, but a tribute'





# enter debug mode, if this file is called directly
if __name__ == "__main__":
    app.run(
        port=9999,
        host='0.0.0.0',
        debug=True
    )
