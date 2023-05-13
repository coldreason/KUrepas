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


@app.route('/taskqueue',methods=['POST'])
def post_taskqueue():
    data = request.json
    task = Task.from_json(json_obj = data)
    db.session.add(task)
    db.session.commit()
    response = make_response("Data received: " + str(data))
    response.status_code = 200
    return response

# 아직 스코어링 요청 작업을 안한 id 대상으로 하나 보내줌
@app.route('/taskqueue',methods=['GET'])
def get_taskqueue():
    tasks = Task.query.filter_by(assigned=False).all()
    if tasks:
        tasks[0].assigned = True
        db.session.commit()
        return jsonify(tasks[0].to_json())
    else:
        return jsonify([])


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

#해당 unit id에 task score 요청
@app.route('/score_request',methods=['POST'])
def register_score_request():
    data = request.json
    requestscore = Requestscore.from_json(json_obj = data)
    db.session.add(requestscore)
    db.session.commit()
    response = make_response("Data received: " + str(data))
    response.status_code = 200
    return response

#해당 unit id에 할당된 score해야할 task있는지 조회
@app.route('/score_request',methods=['GET'])
def get_score_request():
    data = request.json['unit_id']
    requestscores = Requestscore.query.filter_by(unit_id=int(data)).all()
    if requestscores:
        return jsonify(requestscores[0].to_json())
    else:
        return jsonify([])

#스코어 점수 업데이트
@app.route('/score',methods=['POST'])
def post_score():
    data = request.json
    score = Score.from_json(json_obj = data)
    db.session.add(score)
    db.session.commit()
    response = make_response("Data received: " + str(data))
    response.status_code = 200
    return response

#스코어 점수 확인
@app.route('/score',methods=['GET'])
def get_score():
    task_id = request.json['task_id']
    unit_id = request.json['unit_id']
    requestscores = Requestscore.query.filter_by(task_id=int(task_id),unit_id=int(unit_id)).all()
    if requestscores:
        return jsonify(requestscores[0].to_json())
    else:
        return jsonify([])

#자동차 현재 위치 조회 
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

#자동차 현재 위치 업데이트
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