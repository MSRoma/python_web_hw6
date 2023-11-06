SELECT ROUND(AVG(g.grades), 2) as avg , groups_name
FROM grades as g
LEFT JOIN students as s ON g.student_id = s.id
LEFT JOIN subjects as sb ON g.subject_id = sb.id
LEFT JOIN groups as gr ON s.groups_id = gr.id
WHERE gr.id LIKE 1
GROUP BY groups_name
ORDER BY avg desc;