-- script qui liste tous les enregistrements
-- de la table second_table de la base de données hbtn_0c_0
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
