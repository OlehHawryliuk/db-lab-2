import cx_Oracle
import chart_studio.plotly as py
import plotly.graph_objs as go
import re
import chart_studio.dashboard_objs as dashboard


username = 'asd'
password = 'asd'
database = 'localhost/xe'

firstQuery = """
SELECT
sum(price) AS "summary price",
subject
FROM
Udemy_courses group by subject

"""

secondQuery = """

SELECT
COUNT(id) AS "count courses",
level_name
FROM
udemy_courses
GROUP BY
level_name
"""

thirdQuery = """
SELECT
DISTINCT lectures_num,
price
FROM
udemy_courses where
subject = 'Business Finance'
order by lectures_num
"""




def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[A-z0-9]+/[0-9]+", url)[0][1:]
    return raw_fileId.replace('/', ':')


conn = cx_Oracle.connect(username, password, database)
cursor = conn.cursor()

cursor.execute(firstQuery)
count_of_course = []
price = []

for row in cursor:
    count_of_course += [row[0]]
    price += [row[1]]

data = [go.Bar(x=price, y=count_of_course)]
layout = go.Layout(
    title='Загальна ціна курсів де кількість лекцій в заданому проміжку',
    xaxis=dict(
        title='Fire info',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Count of fires',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)

fig = go.Figure(data=data, layout=layout)
price_count = py.plot(fig, filename='price_count')

cursor.execute(secondQuery)

courses = []
level_name = []

for row in cursor:
    courses += [row[0]]
    level_name += [row[1]]

pie = go.Pie(labels=level_name, values=courses)
courses_levels = py.plot([pie], filename='courses_levels')

cursor.execute(thirdQuery)
lectures = []
price_lect = []

for row in cursor:
    lectures += [row[0]]
    price_lect += [row[1]]

lectures_prices = go.Scatter(
    x=price_lect,
    y=lectures,
    mode='lines+markers'
)

data = [lectures_prices]
price_to_lect = py.plot(data, filename='price_to_lect')

my_dboard = dashboard.Dashboard()
price_count = fileId_from_url(price_count)
courses_levels = fileId_from_url(courses_levels)
price_to_lect = fileId_from_url(price_to_lect)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': price_count,
    'title': 'Цена - предмет'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': courses_levels,
    'title': 'Уровень - количество'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': price_to_lect,
    'title': 'Количество лекций - цена'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dboard, 'My First Dashboard with Python')
