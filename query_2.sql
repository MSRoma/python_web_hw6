SELECT fullname
FROM students
where id IN (select student_id
from grades
where subject_id = 5
group by student_id
order by avg(grades) desc limit 1)