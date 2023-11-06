SELECT s.fullname ,ROUND(AVG(g.grades), 2)
FROM grades as g
LEFT JOIN students as s ON g.student_id = s.id
GROUP BY s.fullname
ORDER BY AVG(g.grades) desc limit 5;
