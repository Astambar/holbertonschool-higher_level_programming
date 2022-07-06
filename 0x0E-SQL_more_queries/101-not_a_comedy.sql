-- script qui utilise la base de données hbtn_0d_tvshows pour lister
-- tous les genres non liés au genre Comedy
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN
(
	SELECT tv_genres.name
	FROM tv_genres
	LEFT JOIN tv_show_genres
	ON tv_genres.id=tv_show_genres.genre_id
	LEFT JOIN tv_shows
	ON tv_show_genres.show_id=tv_shows.id
	WHERE tv_genres.name='Comedy'
)
ORDER BY tv_genres.name;