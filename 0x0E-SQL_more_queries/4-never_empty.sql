-- script that creates the table id_not_null on your MySQL server.
-- Creates table if it does not exist and id has a defualt value of 1
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));