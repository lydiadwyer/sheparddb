# sheparddb

[![Code Climate](https://codeclimate.com/github/lydiadwyer/sheparddb/badges/gpa.svg)](https://codeclimate.com/github/lydiadwyer/sheparddb)

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
# open http://127.0.0.1:9999
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
sudo su -
cd /var/www/sheparddb
export PYTHONPATH=$(pwd)

pylint shepard.py --reports=n
pylint ./modules/Countries/controller.py --reports=n

# reset the database, before running tests
# flask unit testing now does this automatically
#sudo su - postgres -c "psql -f /vagrant/psql/db_reset.sql" > /dev/null

# delete all existing .pyc files...
find . -name \*.pyc -delete

# runs all tests in folder and subfolders
nosetests --verbosity=2

# run all tests for sheparddb, show coverage
# http://manpages.ubuntu.com/manpages/trusty/man1/nosetests.1.html
nosetests --with-xcoverage --cover-package=sheparddb \
    -q -x --verbosity=2 --cover-inclusive --no-byte-compile

nosetests --with-xcoverage --cover-package=sheparddb.modules.Countries \
    -q -x --verbosity=2 --cover-inclusive --no-byte-compile

nosetests --with-xcoverage --cover-package=sheparddb.modules.Regions \
    -q -x --verbosity=2 --cover-inclusive --no-byte-compile

nosetests --with-xcoverage --with-xunit --all-modules --traverse-namespace \
    --cover-package=sheparddb --cover-inclusive --cover-erase -x

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





## Selenium

### Install on Ubuntu

```shell
# install Java
sudo apt-get update
sudo apt-get install -y openjdk-7-jre unzip python-dev

# install Selenium Server
# Always use a month(s) old build because the newest never works right
cd ~/Downloads
wget -q http://selenium-release.storage.googleapis.com/2.53/selenium-server-standalone-2.53.0.jar

# install Selenium Chrome driver
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver
wget http://chromedriver.storage.googleapis.com/2.21/chromedriver_linux64.zip
unzip ./chromedriver_linux64.zip
sudo mv ./chromedriver /usr/local/sbin

# install Python lettuce_webdriver
sudo -H pip install lettuce lettuce_webdriver nose python-Levenshtein

# install Python postgres driver
# http://initd.org/psycopg/docs/install.html#installation
sudo apt-get install -y python-psycopg2

```



### Run Tests

```shell
# in host machine
cd ~/Sites/sheparddb/data/selenium

# test that Selenium can be run
python ./selenium_test.py

# run all features
lettuce

# run one feature
lettuce ./features/country.feature

# run a single step, in a feature
lettuce ./features/country.feature -s 1 --failfast

# run individual steps, in a feature
lettuce ./features/country.feature -s 1,2
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
- on failure, log it, and abort()
- review app logs, uwsgi logs, nginx logs, fix errors
- all logs should ideally be clean all the time
- read all the documentation:
    - Flask
        - http://flask.pocoo.org/docs/0.11/
        - http://flask.pocoo.org/docs/0.11/api/
        - http://flask.pocoo.org/docs/0.11/api/#incoming-request-data
        - http://flask.pocoo.org/docs/0.11/api/#response-objects
        - http://flask.pocoo.org/docs/0.11/appcontext/
        - http://flask.pocoo.org/docs/0.11/patterns/appfactories/
    - Blueprints
        - http://flask.pocoo.org/docs/0.11/blueprints/
        - http://flask.pocoo.org/docs/0.11/api/#blueprint-objects
    - Jinja
        - http://jinja.pocoo.org/docs/dev/
    - SQLAlchemy
        - http://docs.sqlalchemy.org/en/latest/
        - http://flask-sqlalchemy.pocoo.org/2.1/api/#models
        - http://stackoverflow.com/questions/31750441/generalised-insert-into-sqlalchemy-using-dictionary
    - Werkzeug
        - http://werkzeug.pocoo.org/docs/0.11/
        - http://werkzeug.pocoo.org/docs/0.11/wrappers/#werkzeug.wrappers.Request
    - uwsgi
        - https://uwsgi-docs.readthedocs.io/en/latest/
    - nginx
        - https://nginx.org/en/docs/
- follow the PEP8 standard
    - https://www.python.org/dev/peps/pep-0008/
- document your code using the Sphinx documetation format
    - http://dolphm.com/pep257-good-python-docstrings-by-example/
    - http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    - http://www.sphinx-doc.org/en/stable/ext/example_google.html
    - https://pythonhosted.org/an_example_pypi_project/sphinx.html#full-code-example
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



## Add a new database table column:

- add new col to db schema
- add example db data
- run database reset script
- add new attribute to the model
- add new attribute to the model __init__ function
- update view one template
- update view all template???
- update the add and edit HTML templates
- update the add and edit functions in controller
- test add
- test edit
- test delete
- test ALL other features (yes really, you may have broken them)
