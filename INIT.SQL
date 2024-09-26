CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    equipment_id VARCHAR(12) NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL, 
    value NUMERIC NOT NULL
);
