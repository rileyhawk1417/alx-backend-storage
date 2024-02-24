-- Calculate the average weighted score for students
-- Extra comment line

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT IF(SUM(score * weight) > 0, SUM(score * weight) / SUM(weight), 0)
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id
    )
END $$
DELIMITER;


