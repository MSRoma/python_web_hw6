SELECT fullname , subjects_name
FROM teachers as t
LEFT JOIN subjects as sb ON t.id = sb.teachers_id
