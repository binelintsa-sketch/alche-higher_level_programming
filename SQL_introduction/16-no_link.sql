-- Lists all records of the table second_table having a name value, ordered by descending score
-- SQL query to select score and name where name is not null or empty
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name != '' 
ORDER BY score DESC;
