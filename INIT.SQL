SET CLIENT_ENCODING = 'UTF8';

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