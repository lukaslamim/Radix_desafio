CREATE TABLE sensors (
    id SERIAL PRIMARY KEY,               
    equipmentId VARCHAR(10) PRIMARY KEY,   
    timestamp TIMESTAMPTZ NOT NULL,      
    value NUMERIC NOT NULL            
);