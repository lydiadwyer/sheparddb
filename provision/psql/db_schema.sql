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
    square_opening          DATE,
    square_closing          DATE,
    square_supervisor       VARCHAR(128) references excavators(excavator_initials),
    field_id                INT references excavation_fields(field_id)
);
COMMENT ON COLUMN excavation_squares.square_size_area
    IS 'The size of a field in meters';
ALTER TABLE excavation_squares OWNER TO shepard;




CREATE TABLE excavation_square_loci(
    locus_id               SERIAL PRIMARY KEY,
    locus_name             VARCHAR(128),
    square_id              INT references excavation_squares(square_id),
    locus_begin_period     VARCHAR(128) references culture_eras(era_name),
    locus_end_period       VARCHAR(128) references culture_eras(era_name),
    z_top                  INT,
    z_bottom               INT,
    locus_depth            INT,
    locus_description      VARCHAR(128),
    locus_association      VARCHAR(128)         
);
ALTER TABLE excavation_square_loci OWNER TO shepard;




CREATE TABLE excavation_square_structure(
    structure_id               SERIAL PRIMARY KEY,
    structure_name             VARCHAR(128),
    structure_description      VARCHAR(128),
    square_id                  INT references excavation_squares(square_id),
    structure_begin_period     VARCHAR(128) references culture_eras(era_name),
    structure_end_period       VARCHAR(128) references culture_eras(era_name)  
);
ALTER TABLE excavation_square_loci OWNER TO shepard;




CREATE TABLE pottery_buckets(
    pottery_bucket_id               SERIAL PRIMARY KEY,
    pottery_bucket_number           INT,
    object_count                    INT,
    pottery_bucket_date             DATE,
    locus_id                        INT references excavation_square_loci(locus_id)
);
ALTER TABLE pottery_buckets OWNER TO shepard;


CREATE TABLE excavators(
    excavator_id               SERIAL PRIMARY KEY,
    excavator_name             VARCHAR(128),
    excavator_initials         VARCHAR(128)
);
ALTER TABLE excavators OWNER TO shepard;




CREATE TABLE excavation_years(
    excavation_year_id               SERIAL PRIMARY KEY,
    excavation_year                  DATE
);
ALTER TABLE excavation_years OWNER TO shepard;




CREATE TABLE storage_locations(
    storage_location_id               SERIAL PRIMARY KEY,
    storage_location_name             VARCHAR(128),
    storage_location_address          VARCHAR(128)
);
ALTER TABLE storage_locations OWNER TO shepard;




CREATE TABLE pottery_buckets(
    pottery_bucket_id               SERIAL PRIMARY KEY,
    pottery_bucket_number           INT,
    pottery_bucket_date             DATE,
    pottery_bucket_count            INT,
    excavator_initials              VARCHAR(128) references excavators(excavator_name),
    square_id                       INT references excavation_squares(square_id),
    locus_id                        INT references excavation_square_loci(locus_id)
);
ALTER TABLE pottery_buckets OWNER TO shepard;




CREATE TABLE excavation_finds(
    find_id                 SERIAL PRIMARY KEY,
    object_reg_id           INT,
    gen_reg_id              INT,
    square_id               INT references excavation_squares(square_id),
    locus_id                INT references excavation_square_loci(locus_id),
    pottery_bucket_id       INT references pottery_buckets(pottery_bucket_id),
    unsure_object           BOOLEAN,
);
ALTER TABLE excavation_finds OWNER TO shepard;



CREATE TABLE material_categories(
    material_id              SERIAL PRIMARY KEY,
    material_type            VARCHAR(128),
    material_name            VARCHAR(128)
);
ALTER TABLE material_categories OWNER TO shepard;




CREATE TABLE ceramic_fabrics(
    ceramic_fabric_id              SERIAL PRIMARY KEY,
    ceramic_fabric_name            VARCHAR(128)
);
ALTER TABLE ceramic_fabrics OWNER TO shepard;




CREATE TABLE ceramic_decorations(
    ceramic_decorations_id              SERIAL PRIMARY KEY,
    ceramic_decorations                 VARCHAR(128)
);
ALTER TABLE ceramic_decorations OWNER TO shepard;










-- Need to add chems, make them individual or oxides?
CREATE TABLE chemical_data(
    data_id                        SERIAL PRIMARY KEY,
    material_name                  VARCHAR(128) references material_categories(material_name),
    find_id                        INT references excavation_finds(find_id)
);
ALTER TABLE chemical_data OWNER TO shepard;




-- Date object cannot go below 4713 BC, consider using INT
CREATE TABLE culture_eras(
    era_id                             SERIAL PRIMARY KEY,
    era_name                           VARCHAR(128),
    era_beginning_date                 DATE,
    era_ending_date                    DATE
);
ALTER TABLE culture_eras OWNER TO shepard;






ALTER DATABASE sheparddb OWNER TO shepard;