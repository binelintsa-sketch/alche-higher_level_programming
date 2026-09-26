-- Lists all records with a score >= 10 in second_table ordered by score (top first)
-- SQL query to select score and name where score is at least 10
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
