#!/bin/bash

# set the session to be noninteractive
export DEBIAN_FRONTEND="noninteractive"

# update apt-get
apt-get update

# install basics
apt-get -q install -y build-essential daemon





## Install Postgres
echo "INFO: Installing Postgres..."

# install
echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" > \
	/etc/apt/sources.list.d/postgres.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
apt-get update
apt-get install -y postgresql-9.5 postgresql-client-9.5 postgresql-contrib-9.5

# configure Postgres
cp /vagrant/psql/postgresql.conf /etc/postgresql/9.5/main/postgresql.conf
cp /vagrant/psql/pg_hba.conf /etc/postgresql/9.5/main/pg_hba.conf
service postgresql restart

# rebuild the database
echo "INFO: Setting up the database..."
su - postgres -c "psql -f /vagrant/psql/db_reset.sql"
service postgresql restart




## Install nginx
echo "INFO: Installing nginx..."

# add the nginx apt-get repo
wget -q -O - http://nginx.org/keys/nginx_signing.key | \
	apt-key add -
echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" > \
	/etc/apt/sources.list.d/nginx.list
apt-get update

# install
apt-get -q install -y nginx=1.10.0*
service nginx restart

# setup logs folder
mkdir -p /var/log/nginx/
chown -R www-data:www-data /var/log/nginx/

# copy over configs, restart
cp -R /vagrant/nginx/* /etc/nginx/
service nginx restart 2>&1




## Install Python
echo "INFO: Installing Python..."

# install, upgrade pip
apt-get -q install -y python=2.7.5* python-dev python-pip \
	libpq-dev python-gi libxml2-dev libxslt-dev libffi-dev libssl-dev
pip install --upgrade pip
pip install requests --upgrade
pip install requests['security']

# install requirements
pip install -qq -r /vagrant/pip_requirements.txt 2>&1





## Install uWSGI
echo "INFO: Installing uWSGI..."

# install
apt-get -q install -y uwsgi uwsgi-plugin-python
service uwsgi restart 2>&1

# init logs
mkdir -p /var/log/sheparddb/
touch /var/log/sheparddb/info.log
chown -R www-data:www-data /var/log/sheparddb

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
