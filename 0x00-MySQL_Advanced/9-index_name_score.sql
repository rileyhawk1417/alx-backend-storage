-- Create a index of the first letter name with their score

CREATE INDEX idx_name_first_score ON names(name(1), score);
