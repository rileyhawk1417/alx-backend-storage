-- Create users table and add country as a column
CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255) NOT NULL UNIQUE, name VARCHAR(255), country NOT NULL ENUM('US', 'CO', 'TN') DEFAULT 'US' );
