#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import psycopg2
# from flask_testing import TestCase
from shepard import create_flask

def reset_database():

    # print 'reset_database()'
    conn = psycopg2.connect(
        "dbname=sheparddb user=shepard host=127.0.0.1 password=shepard")
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(open("/vagrant/psql/db_create_schema.sql", "r").read())
    cursor.execute(open("/vagrant/psql/db_data.sql", "r").read())
    cursor.close()
    conn.close()

def reset_data():

    print 'reset_data()'
    conn = psycopg2.connect(
        "dbname=sheparddb user=shepard host=127.0.0.1 password=shepard")
    conn.autocommit = True
    cursor = conn.cursor()
    # cursor.execute(open("/vagrant/psql/db_create_schema.sql", "r").read())
    cursor.execute(open("/vagrant/psql/db_data.sql", "r").read())
    cursor.close()
    conn.close()

# enter debug mode, if this file is called directly
if __name__ == "__main__":
    reset_database()
