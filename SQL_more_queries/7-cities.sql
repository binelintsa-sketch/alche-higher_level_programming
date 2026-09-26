-- Creates the database hbtn_0d_usa and the table cities with a foreign key constraint
-- Creates database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Uses database hbtn_0d_usa
USE hbtn_0d_usa;

-- Creates table cities if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
