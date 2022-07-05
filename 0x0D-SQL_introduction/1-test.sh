#!/usr/bin/env sh
echo "1-create_database_if_missing.sql"
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

echo "2-remove_database.sql"
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

echo "3-list_tables.sql"
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql

echo "6-list_values.sql"
cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

echo "7-insert_value.sql"
cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
