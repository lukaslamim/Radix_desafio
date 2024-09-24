CREATE TABLE sensor (
    id SERIAL PRIMARY KEY,               
    equipmentId VARCHAR(10) NOT NULL,   
    timestamp TIMESTAMPTZ NOT NULL,      
    value NUMERIC NOT NULL            
);
