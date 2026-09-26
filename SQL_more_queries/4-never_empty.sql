-- Creates the table id_not_null on MySQL server
-- SQL query to create id_not_null table with default id value of 1
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
