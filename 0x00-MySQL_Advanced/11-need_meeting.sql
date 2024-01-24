-- Create a view for students meeting

CREATE VIEW need_meeting AS
SELECT
    students.student_name,
    students.score,
    students.last_meeting
FROM
    students
WHERE
    students.score < 80
    AND (students.last_meeting IS NULL OR DATEDIFF(NOW(), students.last_meeting) > 30);

