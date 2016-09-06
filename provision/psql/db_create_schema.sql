-- Postgres Cheatsheet
-- https://gist.github.com/apolloclark/ea5466d5929e63043dcf

-- Destroy the schema
DROP SCHEMA IF EXISTS sheparddb CASCADE;

-- Setup database schema:
CREATE SCHEMA IF NOT EXISTS sheparddb AUTHORIZATION shepard;
GRANT ALL ON SCHEMA sheparddb TO shepard;





-- Setup database tables;
DROP TABLE IF EXISTS artifacts CASCADE;
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
ALTER FUNCTION set_artifact_created() OWNER TO shepard;

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
ALTER FUNCTION update_artifact_updated() OWNER TO shepard;

CREATE TRIGGER update_artifact_updated_trigger BEFORE UPDATE
    ON artifacts FOR EACH ROW EXECUTE PROCEDURE
    update_artifact_updated();




DROP TABLE IF EXISTS countries CASCADE;
CREATE TABLE countries(
    country_id         SERIAL PRIMARY KEY,
    country_name       VARCHAR(128),
    country_abrev      VARCHAR(128),
    country_created    TIMESTAMP
);
ALTER TABLE countries OWNER TO shepard;




DROP TABLE IF EXISTS regions CASCADE;
CREATE TABLE regions(
    region_id         SERIAL PRIMARY KEY,
    region_name       VARCHAR(128),
    country_id        INT references countries(country_id)
);
ALTER TABLE regions OWNER TO shepard;





-- Add city coordinates?
DROP TABLE IF EXISTS cities CASCADE;
CREATE TABLE cities(
    city_id         SERIAL PRIMARY KEY,
    city_name       VARCHAR(128),
    country_id      INT references countries(country_id),
    region_id       INT references regions(region_id)
);
ALTER TABLE cities OWNER TO shepard;





DROP TABLE IF EXISTS excavations CASCADE;
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