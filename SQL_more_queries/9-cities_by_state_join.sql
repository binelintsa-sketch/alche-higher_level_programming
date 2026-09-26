-- Lists all cities contained in the database hbtn_0d_usa with state names
-- SQL query using an INNER JOIN to display cities.id, cities.name, and states.name
SELECT cities.id, cities.name, states.name 
FROM cities 
JOIN states ON cities.state_id = states.id 
ORDER BY cities.id ASC;
