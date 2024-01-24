-- Create an index for names using the first letter

CREATE INDEX idx_name_first ON names (LEFT(name, 1));
