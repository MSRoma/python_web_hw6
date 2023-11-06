SELECT fullname, g.grades as avg , groups_name , subjects_name
FROM grades as g
LEFT JOIN students as s ON g.student_id = s.id
LEFT JOIN subjects as sb ON g.subject_id = sb.id
LEFT JOIN groups as gr ON s.groups_id = gr.id
WHERE gr.id LIKE 2 AND subject_id LIKE 6
GROUP BY fullname
ORDER BY avg desc;