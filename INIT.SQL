CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    equipment_id VARCHAR(10) NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT now(), 
    value NUMERIC NOT NULL
);
