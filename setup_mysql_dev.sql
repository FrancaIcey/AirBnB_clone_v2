-- Create the database 'hbnb_dev_db' if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Try to create the user 'hbnb_dev'@'localhost' with the password 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to the 'hbnb_dev' user on the 'hbnb_dev_db' database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the 'performance_schema' database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

