# sheparddb

## Install

1. Install Virtualbox and Vagrant
2. git clone this repo
3. open a Terminal, and run "vagrant up"
4. Wait about 10 min
5. open a browser: http://127.0.0.1:8080

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


## Coding Guidelines

Don't use Python virtual environments. They don't really offer robust dependency
isolation, and are an anti-patter in production systems. Instead, just use a
Vagrant VM.

https://pythonrants.wordpress.com/2013/12/06/why-i-hate-virtualenv-and-pip/