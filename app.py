from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('db_test')
def db_test():
    conn = psycopg2.connect("postgres://software_dev_lab_10_db_user:iajeORETZpYisK3P9WSiCJVGIQvVxhE0@dpg-cl5fk7d6fh7c73emhpo0-a/software_dev_lab_10_db")
    conn.close()
    return "Database Connection Successful"
