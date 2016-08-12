-- Postgres Cheatsheet
-- https://gist.github.com/apolloclark/ea5466d5929e63043dcf

-- Drop the database (schema and tables),
-- Create the initial user, set their password:
DROP DATABASE IF EXISTS sheparddb;
DROP USER IF EXISTS shepard;
CREATE USER shepard WITH PASSWORD 'shepard';

-- Create the database:
CREATE DATABASE sheparddb WITH OWNER shepard;
GRANT ALL PRIVILEGES ON DATABASE "sheparddb" TO shepard;

-- Connect to the database:
\c sheparddb;

-- Setup database schema:
CREATE SCHEMA IF NOT EXISTS sheparddb;





-- Setup database tables;
CREATE TABLE artifacts(
    artifact_id         SERIAL PRIMARY KEY,
    artifact_name       VARCHAR(128),
    artifact_obj_reg    INT,
    artifact_created    TIMESTAMP,
    artifact_updated    TIMESTAMP
);
ALTER TABLE artifacts OWNER TO shepard;


-- Setup trigger, to auto-set the created and updated time
CREATE OR REPLACE FUNCTION set_artifact_created()
RETURNS TRIGGER AS $$
BEGIN
   NEW.artifact_created = now();
   NEW.artifact_updated = now();
   RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER set_artifact_created_trigger BEFORE INSERT
    ON artifacts FOR EACH ROW EXECUTE PROCEDURE
    set_artifact_created();

CREATE OR REPLACE FUNCTION update_artifact_updated()
RETURNS TRIGGER AS $$
BEGIN
   NEW.artifact_updated = now();
   RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_artifact_updated_trigger BEFORE UPDATE
    ON artifacts FOR EACH ROW EXECUTE PROCEDURE
    update_artifact_updated();


CREATE TABLE countries(
    country_id         SERIAL PRIMARY KEY,
    country_name       VARCHAR(128),
    country_abrev      VARCHAR(128),
    country_created    TIMESTAMP
);
ALTER TABLE countries OWNER TO shepard;




CREATE TABLE regions(
    region_id         SERIAL PRIMARY KEY,
    region_name       VARCHAR(128),
    country_id        INT references countries(country_id)
);
ALTER TABLE regions OWNER TO shepard;



-- Add city coordinates?
CREATE TABLE cities(
    city_id         SERIAL PRIMARY KEY,
    city_name       VARCHAR(128),
    country_id      INT references countries(country_id),
    region_id       INT references regions(region_id)
);
ALTER TABLE cities OWNER TO shepard;


CREATE TABLE excavations(
    excavation_id         SERIAL PRIMARY KEY,
    excavation_name       VARCHAR(128),
    country_id            INT references countries(country_id),
    region_id             INT references regions(region_id),
    city_id               INT references cities(city_id),
    excavation_created    TIMESTAMP,
    excavation_updated    TIMESTAMP
);
ALTER TABLE excavations OWNER TO shepard;









ALTER DATABASE sheparddb OWNER TO shepard;