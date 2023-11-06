SELECT students.fullname , grades.grades
FROM students  
LEFT JOIN grades ON students.id = grades.student_id
GROUP BY students.fullname
ORDER BY fullname desc limit 3

