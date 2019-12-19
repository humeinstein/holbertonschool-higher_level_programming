-- Count all genres and number of shows
SELECT tv_genres.name AS genre, COUNT(*) AS numbershows
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY numbershows DESC;
