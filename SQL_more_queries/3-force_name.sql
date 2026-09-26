-- Creates the table force_name on MySQL server
-- SQL query to create force_name table if it does not exist with NOT NULL name constraint
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
