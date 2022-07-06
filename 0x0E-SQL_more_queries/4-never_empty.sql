-- script créer une table où les champs ne devrons jamais êtres vide
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
