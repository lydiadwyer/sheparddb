# sheparddb

## Install

1. Install Virtualbox and Vagrant
2. git clone this repo
3. open a Terminal, and run "vagrant up"
4. Wait about 10 min
5. open a browser: http://127.0.0.1:8080





## Debug, run Flask directly

```shell
sudo su -
cd /var/www/sheparddb/
sudo ./shepard.py
# open https://127.0.0.1:9999
```


## Debug, run uWSGI directly
- http://uwsgi.readthedocs.io/en/latest/Configuration.html
- http://uwsgi-docs.readthedocs.io/en/latest/Options.html
- http://uwsgi.readthedocs.io/en/latest/Systemd.html
- http://uwsgi.readthedocs.io/en/latest/Logging.html

```shell
sudo su -
cd /var/www/sheparddb/
sudo uwsgi --plugin http,python --http :8000 \
    --ini /vagrant/config/uwsgi/sheparddb.ini \
    --honour-stdin
```


## Code Quality Checks

```shell
vagrant ssh
cd /var/www/sheparddb
pylint -f ./ > pylint.out
nosetests --with-xcoverage --with-xunit --all-modules --traverse-namespace --cover-package=project --cover-inclusive --cover-erase -x tests.py > /dev/null
clonedigger --cpd-output -o clonedigger.xml project > /dev/null
sloccount --duplicates --wide --details . | fgrep -v .svn > sloccount.sc || :

```


## Reset Database
```shell
su - postgres -c "psql -f /vagrant/psql/db_reset.sql"
```


## System Logs
```shell

# python log
sudo nano /var/log/sheparddb/info.log
watch tail -32 /var/log/sheparddb/info.log

# uwsgi log
sudo nano /var/log/uwsgi/app/sheparddb.log
sudo nano /var/log/uwsgi/app/uwsgi.log

# nginx logs
sudo nano /var/log/nginx/access.log
sudo nano /var/log/nginx/error.log

```



## Postgres

Ensure that you have the Postgres 9.5 client. To install it, on Ubuntu Wily 15.10:

```shell
sudo su -
echo "deb http://apt.postgresql.org/pub/repos/apt/ wily-pgdg main" > \
    /etc/apt/sources.list.d/postgres.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
apt-get update
apt-get install -y postgresql-client-9.5
```

Connect to the database, from host machine:
```shell
psql -U shepard -d sheparddb -h 127.0.0.1 -W
# the password is "shepard"
```

Reset the database, within the guest VM:
```shell
sudo su - postgres -c "psql -f /vagrant/psql/db_reset.sql"
# become the postgres user, and run the command psql, with the file db_reset.sql
```

## Coding Guidlines

Don\'t use Python virtual environments. They don\'t really offer robust dependency
isolation, and are an anti-patter in production systems. Instead, just use a
Vagrant VM.

https://pythonrants.wordpress.com/2013/12/06/why-i-hate-virtualenv-and-pip/

- run pylint, sloccount, radon
- group related functions into a class
- a class should do one thing well
- a class should be less than 500 lines, 20 functions
- a function should be less than 50 lines
- move more than 3 lines of duplicate code into a base class (Push Down)
- use Yoda conditions, ex: (if None is var_name)
- on failure, log it, abort() or return False
- review app logs, uwsgi logs, nginx logs, fix errors
- all logs should ideally be clean all the time
- read all the Flask, Blueprints, Jinja, SQLAlchemy, Werkzeug, uwsgi, nginx
http://flask.pocoo.org/docs/0.11/
http://flask.pocoo.org/docs/0.11/blueprints/
http://jinja.pocoo.org/docs/dev/
http://docs.sqlalchemy.org/en/latest/
http://werkzeug.pocoo.org/docs/0.11/
https://uwsgi-docs.readthedocs.io/en/latest/
https://nginx.org/en/docs/

- follow the PEP8 standard
https://www.python.org/dev/peps/pep-0008/

- document your code using the Sphing documetation format
http://dolphm.com/pep257-good-python-docstrings-by-example/
http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
http://www.sphinx-doc.org/en/stable/ext/example_google.html
https://pythonhosted.org/an_example_pypi_project/sphinx.html#full-code-example

- use the Flask Blueprint Divisional layout
http://exploreflask.com/en/latest/blueprints.html#divisional

```shell
# change the working directory to the website
cd /var/www/sheparddb

# search for a string in files, case insensitive
grep -inr "<string>"

# run linting
pylint ./*.py

```