#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

# create app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


# enter debug mode, if this file is called directly
if __name__ == "__main__":
    app.run(
        port=9999,
        host='0.0.0.0',
        debug=True
    )
