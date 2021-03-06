#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Central Controller class for the ShepardDB website."""

import logging
from logging import Formatter
from logging.handlers import WatchedFileHandler
from flask import Flask, render_template
from mongoengine import QuerySet

from modules.Shared.database import db, mongo


def create_flask():
    """ Create the Flask app """

    # print 'shepard::create_flask()'

    # create app
    app = Flask(__name__)

    # configure settings
    app.config.from_pyfile('config.py')

    # setup SQL database handler
    db.app = app
    db.init_app(app)
    
    # set up mongo database handler
    mongo.app = app
    mongo.init_app(app)


    # configure logger
    # http://flask.pocoo.org/docs/0.11/api/#flask.Flask.logger
    # https://docs.python.org/dev/library/logging.html#logging.Logger
    handler = WatchedFileHandler(app.config['DEBUG_LOG_FILE'])
    handler.setLevel(logging.INFO)
    # http://flask.pocoo.org/docs/0.11/errorhandling/#controlling-the-log-format
    handler.setFormatter(Formatter(
        '%(asctime)s [%(levelname)s] %(message)s '
        '[%(pathname)s : %(lineno)d]'
    ))
    app.logger.addHandler(handler)
    app.logger.setLevel('INFO')

    # register the module controllers
    # sets up URL collections, that we wrote in CONTROLLER file
    from modules.Countries.controller import countries
    from modules.Regions.controller import regions
    from modules.Cities.controller import cities
    from modules.Artifacts.controller import artifacts
    from modules.Excavations.controller import excavations
    from modules.Ceramics.controller import ceramics
    
    app.register_blueprint(artifacts)
    app.register_blueprint(excavations)
    app.register_blueprint(countries)
    app.register_blueprint(regions)
    app.register_blueprint(cities)
    app.register_blueprint(ceramics)

    # http://flask.pocoo.org/docs/0.11/api/#flask.Flask.route
    @app.route('/')
    def home():
        """Default homepage

        Args:
            None
        Returns:
            The homepage HTML. Currently just 'Hello World'.

        """
        return render_template('home.html')

    return app


# enter debug mode, if this file is called directly
if __name__ == "__main__":
    print 'shepard::__main__'
    create_flask().run(
        port=9999,
        host='0.0.0.0',
        debug=True
    )
