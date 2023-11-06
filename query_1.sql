SELECT s.fullname ,ROUND(AVG(g.grades), 2) as avg
FROM grades as g
LEFT JOIN students as s ON g.student_id = s.id
GROUP BY s.fullname
ORDER BY avg desc limit 5;
