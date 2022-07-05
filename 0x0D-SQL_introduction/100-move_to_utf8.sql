-- script qui convertit la base de données hbtn_0c_0 en UTF8
-- (utf8mb4, assembler utf8mb4_unicode_ci) dans votre serveur MySQL
ALTER DATABASE `hbtn_0c_0`
    CHARACTER SET `utf8mb4`
    COLLATE `utf8mb4_unicode_ci`;

USE `hbtn_0c_0`;

ALTER TABLE `first_table`
    CONVERT TO CHARACTER SET `utf8mb4`
    COLLATE `utf8mb4_unicode_ci`;