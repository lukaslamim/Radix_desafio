CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    equipment_id VARCHAR(12) NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL, 
    value NUMERIC NOT NULL
);

CREATE TABLE sensor_user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) NOT NULL,
    password VARCHAR(128) NOT NULL 
);

INSERT INTO sensor_user (username, password) VALUES('admin', '$2b$12$rXaN9EJUhLDZ3TRSkJNRv.YhmRo50d3F9ujn4DIYKE3fndkU7/m5W');
