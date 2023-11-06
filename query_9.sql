SELECT fullname, subjects_name
FROM students as s
LEFT JOIN grades as g ON s.id = g.student_id
LEFT JOIN subjects as sb ON g.subject_id = sb.id
WHERE s.id LIKE 3
GROUP BY subjects_name
