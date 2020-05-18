import csv

import cx_Oracle

username = 'asd'
password = 'asd'
database = 'localhost/xe'
tableNames = ['Course', 'Info', 'Udemy', 'Subject']

conn = cx_Oracle.connect(username, password, database)

cursor = conn.cursor()


try:
    for el in tableNames:
        with open(el+'.csv', 'w', newline='') as newCsvFile:
            cursor.execute("SELECT * FROM " + el)

            titles = []

            for row in cursor.description:
                titles.append(row[0])
            csvWriter=csv.writer(newCsvFile, delimiter=',')
            csvWriter.writerow(titles)

            for row in cursor:
                csvWriter.writerow(row)
finally:
    cursor.close()
    conn.close()