import csv
import sys

import cx_Oracle
import io
username = 'crispyyv'
password = '19680401'
database = 'localhost/xe'
filename="udemy_courses.csv"

connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

with io.open(filename, encoding="utf8") as file:
    reader = csv.DictReader(file)
    i=1

    try:
        for row in reader:



            course_id = int(row['course_id'])
            name = row['course_title']
            url = row['url']
            price = float(row['price'])
            lectures_num = int(row['num_lectures'])
            level = row['level']
            duration = float(row['content_duration'])
            subject = row['subject']


            insert = """ INSERT /*+ IGNORE_ROW_ON_DUPKEY_INDEX (Course (id)) */ INTO Course(id, name, url, price) VALUES(:course_id, :name, :url, :price)"""
            cursor.execute(insert, course_id=course_id, name=name, url=url, price=price)

            insert = """INSERT /*+ IGNORE_ROW_ON_DUPKEY_INDEX (Info (id)) */ INTO Info(id, lectures_num, level_name, duration, course_id)
             VALUES(:id, :lectures_num, :level_name, :duration, :course_id)
"""
            cursor.execute(insert, id=i, lectures_num=lectures_num, level_name=level, duration=duration, course_id=course_id)

            insert = """insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX (Subject (subject)) */ into Subject values(:subject)"""
            cursor.execute(insert, subject=subject)

            insert = """
                insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX (Udemy (id)) */ into Udemy(id, course_id, subject) values(:id, :course_id, :subject)

            """
            cursor.execute(insert, id=i, course_id=course_id, subject=subject)

            i += 1



    except:
        print(f"Error in line: {i}")
        raise

connection.commit()
cursor.close()
connection.close()