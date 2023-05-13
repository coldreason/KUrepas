from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models.user import User
from models.task import Task
from models.designate import Designate
from models.requestscore import Requestscore
from models.currentpos import Currentpos
from models.score import Score
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

@app.route('/get_task/<taskId>',methods=['GET'])
def get_task(taskId):
    task = Task.query.filter_by(id=int(taskId)).all()[0]
    return jsonify(task.to_json())


@app.route('/register_task',methods=['POST'])
def register_task():
    data = request.json
    task = Task.from_json(json_obj = data)
    db.session.add(task)
    db.session.commit()
    response = make_response("Data received: " + str(data))
    response.status_code = 200
    return response

@app.route('/score_request',methods=['POST'])
def register_score_request():
    data = request.json
    requestscore = Requestscore.from_json(json_obj = data)
    db.session.add(requestscore)
    db.session.commit()
    response = make_response("Data received: " + str(data))
    response.status_code = 200
    return response

@app.route('/score_request',methods=['GET'])
def get_all_score_request():
    requestscores = Requestscore.query.all()

    requestscores_list = []
    for requestscore in requestscores:
        requestscores_list.append(requestscore.to_json())

    # Return a JSON response with the list of tasks
    return jsonify(requestscores_list)

@app.route('/score',methods=['GET'])
def get_score():
    data = request.json['id']
    requestscores = Requestscore.query.filter_by(id=int(data)).all()
    if requestscores:
        return jsonify(requestscores[0].to_json())
    else:
        return jsonify([])
    
@app.route('/current_pos',methods=['GET'])
def get_pos():
    data = request.json['unit_id']
    currentpos_list = Currentpos.query.filter_by(unit_id=int(data)).all()
    if not currentpos_list:
        currentpos = Currentpos()
        currentpos.unit_id = data
        currentpos.pos_x = "0"
        currentpos.pos_y = "0"
        db.session.add(currentpos)
        db.session.commit()
        currentpos_list.append(currentpos)
    currentpos = currentpos_list[0]
    return jsonify(currentpos.to_json())

@app.route('/current_pos',methods=['POST'])
def post_pos():
    data = request.json
    currentposs = Currentpos.query.filter_by(unit_id=int(data['unit_id'])).all()
    currentpos = Currentpos.from_json(json_obj = data)
    if currentposs:
        currentposs[0].pos_x = currentpos.pos_x
        currentposs[0].pos_y = currentpos.pos_y
    else:
        db.session.add(currentpos)
    db.session.commit()
    response = make_response("Data received: " + str(data))
    response.status_code = 200
    return response