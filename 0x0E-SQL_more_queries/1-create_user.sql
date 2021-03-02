-- script that creates the MySQL server user user_0d_1
-- This script checks to see if the USER exits and sets a password and give all priviliges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILIGES ON *.* TO 'user_0d_1'@'localhost';