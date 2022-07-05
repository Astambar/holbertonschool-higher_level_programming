-- script qui affiche la température moyenne (Fahrenheit) par ville classée par température (décroissant)
SELECT `city`, AVG( `value` ) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;