-- Lists all genres of the show Dexter from the hbtn_0d_tvshows database
-- SQL query joining tv_genres, tv_show_genres, and tv_shows filtered by show title
SELECT tv_genres.name 
FROM tv_genres 
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id 
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id 
WHERE tv_shows.title = 'Dexter' 
ORDER BY tv_genres.name ASC;
