CREATE OR REPLACE VIEW Udemy_courses as 
    SELECT 
        course.price,
        subject.subject,
         info.level_name,
         udemy.id,
         info.lectures_num
         FROM udemy
     INNER JOIN subject ON udemy.subject = subject.subject
    INNER JOIN course ON course.id = udemy.course_id
     INNER JOIN info ON info.course_id = udemy.course_id;
    