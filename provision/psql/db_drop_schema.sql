-- Close any open connections to the database
SELECT pg_terminate_backend(pid) from pg_stat_activity where datname='sheparddb';



-- Drop the database (schema and tables),
-- Create the initial user, set their password:
DROP DATABASE IF EXISTS sheparddb;
DROP USER IF EXISTS shepard;
CREATE USER shepard WITH PASSWORD 'shepard';

-- Create the database:
CREATE DATABASE sheparddb WITH OWNER shepard;
GRANT ALL PRIVILEGES ON DATABASE "sheparddb" TO shepard;
