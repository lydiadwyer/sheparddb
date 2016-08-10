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





CREATE TABLE excavations(
    excavation_id         SERIAL PRIMARY KEY,
    excavation_name       VARCHAR(128)
);
ALTER TABLE excavations OWNER TO shepard;





CREATE TABLE countries(
    country_id         SERIAL PRIMARY KEY,
    country_name       VARCHAR(128)
);
ALTER TABLE countries OWNER TO shepard;




CREATE TABLE regions(
    region_id         SERIAL PRIMARY KEY,
    region_name       VARCHAR(128),
    country_id        INT references countries(country_id)
);
ALTER TABLE regions OWNER TO shepard;




CREATE TABLE cities(
    city_id         SERIAL PRIMARY KEY,
    city_name       VARCHAR(128),
    country_id      INT references countries(country_id),
    region_id       INT references regions(region_id)
);
ALTER TABLE cities OWNER TO shepard;



CREATE TYPE size_units AS ENUM ('meters', 'feet');
CREATE TABLE excavation_fields(
    field_id         SERIAL PRIMARY KEY,
    field_name       VARCHAR(128),
    field_size_length      INT,
    field_size_width       INT,
    field_size_area        INT,
    field_size_units       size_units
);
ALTER TABLE excavation_fields OWNER TO shepard;




CREATE TABLE excavation_squares(
    square_id               SERIAL PRIMARY KEY,
    square_name             VARCHAR(128),
    square_size_length      INT,
    square_size_width       INT,
    square_size_area        INT,
    square_size_units       size_units,
    field_id                INT references excavation_fields(field_id)
);
COMMENT ON COLUMN excavation_squares.square_size_area
    IS 'The size of a field in meters';
ALTER TABLE excavation_squares OWNER TO shepard;




CREATE TABLE excavation_square_loci(
    locus_id               SERIAL PRIMARY KEY,
    locus_name             VARCHAR(128),
    square_id              INT references excavation_squares(square_id)
);
ALTER TABLE excavation_square_loci OWNER TO shepard;




CREATE TABLE excavators(
    excavator_id               SERIAL PRIMARY KEY,
    excavator_name             VARCHAR(128)
);
ALTER TABLE excavators OWNER TO shepard;




CREATE TABLE excavation_years(
    excavation_year_id               SERIAL PRIMARY KEY,
    excavator_year                   INT
);
ALTER TABLE excavation_years OWNER TO shepard;





CREATE TABLE storage_locations(
    storage_location_id               SERIAL PRIMARY KEY,
    storage_location_name             VARCHAR(128),
    storage_location_address          VARCHAR(128)
);
ALTER TABLE storage_locations OWNER TO shepard;





CREATE TABLE excavation_objects(
    object_id               SERIAL PRIMARY KEY,
    object_reg_id           INT,
    gen_reg_id              INT,
    square_id               INT references excavation_squares(square_id),
    locus_id                INT references excavation_square_loci(locus_id)
);
ALTER TABLE excavation_objects OWNER TO shepard;
















ALTER DATABASE sheparddb OWNER TO shepard;