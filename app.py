"""
Author: Charlie Bailey
Purpose: This file creates a Flask application and provides routes to test database connectivity, create a database table, insert data into the table, select data out of the table, and finally drop the table. This app is being tested and deployed using the Render web hosting service.
"""

from flask import Flask
import psycopg2
app = Flask(__name__)

# Route: '/'
# Description: Returns a simple 'Hello, World!' string.
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Route: '/db_test'
# Description: Tests database connectivity by opening and closing a connection.
@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://software_dev_lab_10_db_user:iajeORETZpYisK3P9WSiCJVGIQvVxhE0@dpg-cl5fk7d6fh7c73emhpo0-a/software_dev_lab_10_db")
    conn.close()
    return "Database Connection Successful"

# Route: '/db_create'
# Description: Creates a 'Basketball' table in the database if it doesn't already exist.
@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgres://software_dev_lab_10_db_user:iajeORETZpYisK3P9WSiCJVGIQvVxhE0@dpg-cl5fk7d6fh7c73emhpo0-a/software_dev_lab_10_db")
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Basketball(
                    First varchar(255),
                    Last varchar(255),
                    City varchar(255),
                    Name varchar(255),
                    Number int
                    );
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

# Route: '/db_insert'
# Description: Inserts player data into the 'Basketball' table.
@app.route('/db_insert')
def insert():
    conn = psycopg2.connect("postgres://software_dev_lab_10_db_user:iajeORETZpYisK3P9WSiCJVGIQvVxhE0@dpg-cl5fk7d6fh7c73emhpo0-a/software_dev_lab_10_db")
    cur = conn.cursor()
    cur.execute('''
                INSERT INTO Basketball (First, Last, City, Name, Number)
                Values
                ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
                ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
                ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
                ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

# Route: '/db_select'
# Description: Selects all of the data in the 'Basketball' table and returns it in a table format.
@app.route('/db_select')
def select():
    conn = psycopg2.connect("postgres://software_dev_lab_10_db_user:iajeORETZpYisK3P9WSiCJVGIQvVxhE0@dpg-cl5fk7d6fh7c73emhpo0-a/software_dev_lab_10_db")
    cur = conn.cursor()
    cur.execute('''
                SELECT * FROM Basketball;
                ''')
    records = cur.fetchall()
    conn.close()
    response_string = ""
    response_string += "<table>"
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += "<td>{}</td>".format(info)
        response_string += "</tr>"
    response_string += "</table>"
    return response_string

# Route: '/db_drop'
# Description: Drops the 'Basketball' table.
@app.route('/db_drop')
def drop():
    conn = psycopg2.connect("postgres://software_dev_lab_10_db_user:iajeORETZpYisK3P9WSiCJVGIQvVxhE0@dpg-cl5fk7d6fh7c73emhpo0-a/software_dev_lab_10_db")
    cur = conn.cursor()
    cur.execute('''
                DROP TABLE Basketball;
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"