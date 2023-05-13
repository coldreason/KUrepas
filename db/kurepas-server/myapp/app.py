from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models.user import User
from models.task import Task
from flask_cors import CORS

from db import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Create a cursor object to interact with the database

with app.app_context():
    db.create_all()

@app.route('/')
def get_all_task():
    # Execute a query to retrieve all tasks from the database
    tasks = Task.query.all()

    # Create a list of dictionaries from the query results
    task_list = []
    for task in tasks:
        task_list.append(task.to_json())

    # Return a JSON response with the list of tasks
    return jsonify(task_list)


@app.route('/register_task',methods=['POST'])
def register_task():
    data = request.json
    data['done'] = False;
    task = Task.from_json(json_obj = data)
    db.session.add(task)
    db.session.commit()
    response = make_response("Data received: " + str(data))
    response.status_code = 200
    return response
