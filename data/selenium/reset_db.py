#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2

# you must have psql installed for this to work
def reset_database():

    conn = psycopg2.connect("dbname=sheparddb user=shepard host=127.0.0.1 password=shepard")
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(open("../../provision/psql/db_create_schema.sql", "r").read())
    cursor.execute(open("../../provision/psql/db_data.sql", "r").read())
    cursor.close()
    conn.close()

if __name__ == "__main__":
    reset_database()
