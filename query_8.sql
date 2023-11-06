SELECT fullname , ROUND(AVG(g.grades), 2) as avg , subjects_name
FROM teachers as t
LEFT JOIN subjects as sb ON t.id = sb.teachers_id
LEFT JOIN grades as g ON sb.id = g.subject_id
WHERE t.id LIKE 2
GROUP BY subjects_name
ORDER BY avg desc;