-- script qui affiche la température moyenne (Fahrenheit)
-- par ville classée par température (décroissant)
SELECT `city`, AVG( `value` ) AS `tempAVG`
FROM `temperatures`
GROUP BY `city`
ORDER BY `tempAVG` DESC;