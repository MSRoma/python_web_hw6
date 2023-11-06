SELECT fullname, ROUND(AVG(g.grades), 2) as avg , subjects_name
FROM grades as g
LEFT JOIN students as s ON g.student_id = s.id
LEFT JOIN subjects as sb ON g.subject_id = sb.id
WHERE subject_id LIKE 5
GROUP BY s.fullname
ORDER BY avg desc;