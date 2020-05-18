DECLARE
    itmes INT := 10;
BEGIN
    FOR i IN 1..itmes LOOP
        INSERT INTO course (
            id,
            name,
            url,
            price
        ) VALUES (
            i,
            i || ' course',
            i || ' url',
            100 + i * 10
        );

        INSERT INTO info (
            id,
            lectures_num,
            level_name,
            duration,
            course_id
        ) VALUES (
            i,
            i * 10,
            'begginer',
            i + 1.5,
            i
        );

        INSERT INTO udemy (
            id,
            course_id,
            subject
        ) VALUES (
            i,
            i,
            'busines'
        );

    END LOOP;
END;