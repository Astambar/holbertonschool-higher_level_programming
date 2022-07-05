-- script qui affiche le top 3 des températures des
-- villes en juillet et août classés par température (décroissant)
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state` ASC;