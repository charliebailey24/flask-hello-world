"""
Author: Charlie Bailey
Purpose: This file creates a Flask application and provides routes to test database connectivity, create a database table, insert data into the table, select data out of the table, and finally drop the table. This is being tested and deployed using the Render web hosting service.
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

# db_insert

# db_select

# db_drop