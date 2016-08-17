#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess, os, time

def reset_database():

    print("Resetting the database...")

    # setup calls
    psql = ['/usr/bin/psql', '-U', 'postgres', '-h', '127.0.0.1']
    psql_str = '/usr/bin/psql -U postgres -h 127.0.0.1 '
    FNULL = open(os.devnull, 'w')

    subprocess.call(
        psql_str + '-f ../../provision/psql/db_schema.sql',
        shell=True,
        env={'PGPASSWORD': 'postgres'},
        stdout=FNULL, stderr=subprocess.STDOUT
    )

    time.sleep(1)

    subprocess.call(
        psql_str + '-d sheparddb -f ../../provision/psql/db_data.sql',
        shell=True,
        env={'PGPASSWORD': 'postgres'},
        stdout=FNULL, stderr=subprocess.STDOUT
    )

if __name__ == "__main__":
    reset_database()
