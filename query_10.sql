SELECT s.fullname, subjects_name , t.fullname
FROM grades as g
LEFT JOIN students as s ON g.student_id = s.id
LEFT JOIN subjects as sb ON g.subject_id = sb.id
LEFT JOIN teachers as t ON sb.teachers_id = t.id
WHERE s.id LIKE 25 AND t.id LIKE 1
GROUP BY subjects_name