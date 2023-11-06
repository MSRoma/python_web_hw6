SELECT ROUND(AVG(g.grades), 2), s.fullname 
FROM grades as g
LEFT JOIN students as s ON g.student_id = s.id
GROUP BY s.fullname 
ORDER BY fullname desc limit 3;