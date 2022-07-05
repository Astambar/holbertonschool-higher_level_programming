-- script qui liste le nombre d'enregistrements avec le même score dans
-- la table second_table de la base de données hbtn_0c_0
SELECT score,COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
