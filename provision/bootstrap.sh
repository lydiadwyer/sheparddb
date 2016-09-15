#!/bin/bash

# set the session to be noninteractive
export DEBIAN_FRONTEND="noninteractive"

# update apt-get
apt-get update

# install basics
apt-get -q install -y build-essential daemon






## Install MongoDB
echo "INFO: Installing MongoDB..."

# install
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" \
	| tee /etc/apt/sources.list.d/mongodb-org-3.2.list
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
apt-get update
apt-get install -y mongodb-org=3.2.9 2>&1
service mongod restart





## Install Postgres
echo "INFO: Installing Postgres..."

# install
echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" > \
	/etc/apt/sources.list.d/postgres.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
	apt-key add -
apt-get update
apt-get install -y postgresql-9.5 postgresql-client-9.5 \
	postgresql-contrib-9.5 2>&1

# configure Postgres
# INSECURE!!!
cp /vagrant/psql/postgresql.conf /etc/postgresql/9.5/main/postgresql.conf
cp /vagrant/psql/pg_hba.conf /etc/postgresql/9.5/main/pg_hba.conf
service postgresql restart

# rebuild the database
echo "INFO: Setting up the database..."
# INSECURE!!!
su - postgres -c "psql -c \"ALTER USER postgres with encrypted password 'postgres';\""
su - postgres -c "psql -f /vagrant/psql/db_reset.sql"
service postgresql restart




## Install nginx
echo "INFO: Installing nginx..."

# add the nginx apt-get repo
echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" > \
	/etc/apt/sources.list.d/nginx.list
wget -q -O - http://nginx.org/keys/nginx_signing.key | \
	apt-key add -
apt-get update

# install
apt-get -q install -y nginx=1.10.0*
service nginx restart

# setup logs folder
mkdir -p /var/log/nginx/
chown -R www-data:www-data /var/log/nginx/

# copy over configs, restart
# INSECURE!!!
cp -R /vagrant/nginx/* /etc/nginx/
service nginx restart 2>&1




## Install Python
echo "INFO: Installing Python..."

# install, upgrade pip
apt-get -q install -y python=2.7.5* python-dev python-pip \
	libpq-dev python-gi libxml2-dev libxslt-dev libffi-dev libssl-dev
pip install pip requests --upgrade
pip install requests['security']

# install code quality tools
pip install -qqq pylint 2>&1
pip install --quiet mock coverage nose nosexcover clonedigger

# install requirements
pip install -r /vagrant/pip_requirements.txt 2>&1





## Install uWSGI
echo "INFO: Installing uWSGI..."

# install
apt-get -q install -y uwsgi uwsgi-plugin-python
service uwsgi restart 2>&1

# init logs
mkdir -p /var/log/sheparddb/
touch /var/log/sheparddb/info.log
chown -R www-data:www-data /var/log/sheparddb
chmod 0777 /var/log/sheparddb/info.log # INSECURE!!!

mkdir -p /var/log/uwsgi/app
chown -R www-data:www-data /var/log/uwsgi/app

# config www-data user shell
chsh -s /bin/bash www-data

# copy over configs, restart
cp /vagrant/uwsgi/* /etc/uwsgi/apps-enabled/
service uwsgi restart 2>&1



# update file location database
updatedb

exit;
