-- Create a trigger function for insert on orders table

DELIMITER //
CREATE TRIGGER after_insert AFTER INSERT ON orders
FOR EACH ROW BEGIN
    UPDATE items SET quantity = quantity - 1 WHERE name = orders.item_name;
END;
DELIMITER;
