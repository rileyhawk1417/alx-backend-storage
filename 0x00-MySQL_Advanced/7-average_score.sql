-- Calculate the average score for users
-- after calculation then store the score.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score INT DEFAULT 0;
    DECLARE projects_count INT DEFAULT 0;
    SELECT SUM(score)
        INTO total_score
        FROM corrections
        WHERE corrections.user_id = user_id;

    SELECT SUM(*)
        INTO total_score
        FROM corrections
        WHERE corrections.user_id = user_id;
    
    UPDATE users
        SET users.average_score = IF(projects_count = 0, 0, total_score / projects_count)
        WHERE users.id = user_id;
END $$
DELIMITER;
