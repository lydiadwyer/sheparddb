INSERT INTO artifacts(artifact_name, artifact_obj_reg) VALUES('test1', 111);
INSERT INTO artifacts(artifact_name, artifact_obj_reg) VALUES('test2', 112);
INSERT INTO artifacts(artifact_name, artifact_obj_reg) VALUES('test3', 113);


INSERT INTO excavations(excavation_name) VALUES('Idalion');
INSERT INTO excavations(excavation_name) VALUES('Wine Cave');
INSERT INTO excavations(excavation_name) VALUES('Catal Houyouk');

INSERT INTO countries(country_name) VALUES('Cyprus');
INSERT INTO countries(country_name) VALUES('France');
INSERT INTO countries(country_name) VALUES('Turkey');

INSERT INTO regions(region_name, country_id) VALUES('Dali', 1);
INSERT INTO regions(region_name, country_id) VALUES('Loire Valley', 2);
INSERT INTO regions(region_name, country_id) VALUES('Ankara', 3);

INSERT INTO cities(city_name, country_id, region_id) VALUES('Dali', 1, 1);
INSERT INTO cities(city_name, country_id, region_id) VALUES('Tours', 2, 2);
INSERT INTO cities(city_name, country_id, region_id) VALUES('Istanbul', 3, 3);