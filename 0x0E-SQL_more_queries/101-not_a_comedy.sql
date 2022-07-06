-- script qui utilise la base de données hbtn_0d_tvshows pour lister
-- tous les genres non liés au genre Comedy
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN
(
	SELECT tv_shows.title
	FROM tv_shows
	LEFT JOIN tv_show_genres
	ON tv_shows.id=tv_show_genres.show_id
	LEFT JOIN tv_genres
	ON tv_show_genres.genre_id=tv_genres.id
	WHERE tv_genres.name='Comedy'
)
ORDER BY tv_shows.title;