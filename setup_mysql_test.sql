-- Create the database 'hbnb_test_db' if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Try to create the user 'hbnb_test'@'localhost' with the password 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the 'hbnb_test' user on the 'hbnb_test_db' database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the 'performance_schema' database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

