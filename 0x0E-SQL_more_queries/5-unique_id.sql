-- script that creates the table unique_id on your MySQL server.
-- This creates a table if it does not exists and created the id default to 1 and has to be unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));