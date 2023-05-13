import mysql.connector
from flask import Flask, jsonify


app = Flask(__name__)

# MySQL connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password12!",
    database="kurepas"
)

# Create a cursor object to interact with the database
mycursor = mydb.cursor()

@app.route('/')
def index():
    # Execute a query to retrieve all users from the database
    mycursor.execute("SELECT * FROM users;")
    users = mycursor.fetchall()
    
    # Create a list of dictionaries from the query results
    user_list = []
    for user in users:
        user_dict = {'id': user[0], 'name': user[1], 'email': user[2]}
        user_list.append(user_dict)
    
    # Return the list of users as JSON
    return jsonify(users=user_list)


# @app.route('/register_task')
# def index():
#     # Execute a query to retrieve all users from the database
#     mycursor.execute("SELECT * FROM users;")
#     users = mycursor.fetchall()
    
#     # Create a list of dictionaries from the query results
#     user_list = []
#     for user in users:
#         user_dict = {'id': user[0], 'name': user[1], 'email': user[2]}
#         user_list.append(user_dict)
    
#     # Return the list of users as JSON
#     return jsonify(users=user_list)