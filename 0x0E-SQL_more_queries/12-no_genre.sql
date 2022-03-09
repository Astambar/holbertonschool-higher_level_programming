-- script créer la database puis génére la table
SELECT ts.title, tsg.genre_id FROM tv_shows ts LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id WHERE genre_id IS NULL ORDER BY ts.title, tsg.genre_id;
