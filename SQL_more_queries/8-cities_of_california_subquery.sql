-- Lists all the cities of California that can be found in hbtn_0d_usa without using JOIN
-- SQL query to select cities of California using a subquery for state_id
SELECT id, name 
FROM cities 
WHERE state_id = (
    SELECT id 
    FROM states 
    WHERE name = 'California'
) 
ORDER BY id ASC;
