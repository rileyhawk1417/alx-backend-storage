-- Create a trigger function for update on users table

DELIMITER //
CREATE TRIGGER before_update BEFORE UPDATE ON users
FOR EACH ROW BEGIN
    SET users.valid_email = 0 WHERE name = users.email;
END;
DELIMITER;
