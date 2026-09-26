-- Lists all shows contained in hbtn_0d_tvshows without a genre linked
-- SQL query using LEFT JOIN to filter for shows where genre_id IS NULL
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
WHERE tv_show_genres.genre_id IS NULL 
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
