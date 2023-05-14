import json
import requests
import torch
import torch.nn as nn
import random
import time
import numpy as np

data = {"unit_id": "1", "pos_x": "3.0", "pos_y": "2.0"}
response_request = requests.post("http://172.20.10.3:5000/current_pos", json = data)
request_data = response_request.json

data = {"unit_id": "2", "pos_x": "2.0", "pos_y": "1.0"}
response_request = requests.post("http://172.20.10.3:5000/current_pos", json = data)
request_data = response_request.json

data = {"unit_id": "3", "pos_x": "1.0", "pos_y": "4.0"}
response_request = requests.post("http://172.20.10.3:5000/current_pos", json = data)
request_data = response_request.json

data = {"unit_id": "4", "pos_x": "3.0", "pos_y": "7.0"}
response_request = requests.post("http://172.20.10.3:5000/current_pos", json = data)
request_data = response_request.json

data = {"unit_id": "5", "pos_x": "6.0", "pos_y": "3.0"}
response_request = requests.post("http://172.20.10.3:5000/current_pos", json = data)
request_data = response_request.json 

data = {"unit_id": "1", "task_id": "3"}
response_request = requests.post("http://172.20.10.3:5000/score_request", json = data)
request_data = response_request.json

response = requests.get("http://172.20.10.3:5000/")
task_data = response.json()  
                                         
id_data = {"unit_id": "1"}
response_request = requests.get("http://172.20.10.3:5000/current_pos", json = id_data)
request_data = response_request.json()

def get_pos_s_x_by_id(data, id):
    for item in data:
        if item['id'] == id:
            return item['pos_s_x']
    return '0'

def get_pos_s_y_by_id(data, id):
    for item in data:
        if item['id'] == id:
            return item['pos_s_y']
    return '0'
def get_pos_e_x_by_id(data, id):
    for item in data:
        if item['id'] == id:
            return item['pos_e_x']
    return '0'

def get_pos_e_y_by_id(data, id):
    for item in data:
        if item['id'] == id:
            return item['pos_e_y']
    return '0'

def get_pos_x_as_integer(unit_id):
    data = {"unit_id": unit_id}
    response = requests.get("http://172.20.10.3:5000/current_pos", json=data)
    request_data = response.json()
    
    pos_x = int(round(float(request_data["pos_x"])))
    return pos_x

def get_pos_y_as_integer(unit_id):
    data = {"unit_id": unit_id}
    response = requests.get("http://172.20.10.3:5000/current_pos", json=data)
    request_data = response.json()
    
    pos_y = int(round(float(request_data["pos_y"])))
    return pos_y

def get_random_float(start, end):
    return round(random.uniform(start, end), 1)

def get_random_integer(start, end):
    return random.randint(start, end)

class PerformanceEvaluator(nn.Module):
    def __init__(self):
        super(PerformanceEvaluator, self).__init__()
        self.conv = nn.Conv1d(6, 16, kernel_size=1)
        self.transformer = nn.TransformerEncoderLayer(d_model=16, nhead=4)
        self.linear = nn.Linear(1, 1) 
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = x.unsqueeze(2)
        x = self.conv(x) 
        x = x.squeeze(2)  
        x = self.transformer(x) 
        x = torch.mean(x, dim=1, keepdim=True) 
        x = self.linear(x)  
        x = self.sigmoid(x) 
        return x

def evaluate_courier_performance(courier):
    model = PerformanceEvaluator()

    inputs = torch.tensor([
        [courier.start_x, courier.start_y, courier.end_x, 
         courier.end_y, courier.current_x, courier.current_y]
    ], dtype=torch.float)

    score = model(inputs)

    return score.item()

class Courier:
    def __init__(self, start_x, start_y, end_x, end_y, current_x, current_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.current_x = current_x
        self.current_y = current_y

unit_id_1 = 1
unit_id_2 = 2
unit_id_3 = 3
unit_id_4 = 4
unit_id_5 = 5

while True:
  task_id_1 = np.random.randint(2,4)
  task_id_2 = np.random.randint(2,4)
  task_id_3 = np.random.randint(2,4)
  task_id_4 = np.random.randint(2,4)
  task_id_5 = np.random.randint(2,4)

  start_x_1 = int(get_pos_s_x_by_id(task_data, task_id_1))
  start_y_1 = int(get_pos_s_y_by_id(task_data, task_id_1))
  end_x_1 = int(get_pos_e_x_by_id(task_data, task_id_1))
  end_y_1 = int(get_pos_e_y_by_id(task_data, task_id_1))
  current_x_1 = int(get_pos_x_as_integer(unit_id_1)) 
  current_y_1 = int(get_pos_x_as_integer(unit_id_1))   

  start_x_2 = int(get_pos_s_x_by_id(task_data, task_id_2))
  start_y_2 = int(get_pos_s_y_by_id(task_data, task_id_2))
  end_x_2 = int(get_pos_e_x_by_id(task_data, task_id_2))
  end_y_2 = int(get_pos_e_y_by_id(task_data, task_id_2))
  current_x_2 = int(get_pos_x_as_integer(unit_id_2)) 
  current_y_2 = int(get_pos_x_as_integer(unit_id_2))  

  start_x_3 = int(get_pos_s_x_by_id(task_data, task_id_3))
  start_y_3 = int(get_pos_s_y_by_id(task_data, task_id_3))
  end_x_3 = int(get_pos_e_x_by_id(task_data, task_id_3))
  end_y_3 = int(get_pos_e_y_by_id(task_data, task_id_3))
  current_x_3 = int(get_pos_x_as_integer(unit_id_3)) 
  current_y_3 = int(get_pos_x_as_integer(unit_id_3))

  start_x_4 = int(get_pos_s_x_by_id(task_data, task_id_4))
  start_y_4 = int(get_pos_s_y_by_id(task_data, task_id_4))
  end_x_4 = int(get_pos_e_x_by_id(task_data, task_id_4))
  end_y_4 = int(get_pos_e_y_by_id(task_data, task_id_4))
  current_x_4 = int(get_pos_x_as_integer(unit_id_4)) 
  current_y_4 = int(get_pos_x_as_integer(unit_id_4))  

  start_x_5 = int(get_pos_s_x_by_id(task_data, task_id_5))
  start_y_5 = int(get_pos_s_y_by_id(task_data, task_id_5))
  end_x_5 = int(get_pos_e_x_by_id(task_data, task_id_5))
  end_y_5 = int(get_pos_e_y_by_id(task_data, task_id_5))
  current_x_5 = int(get_pos_x_as_integer(unit_id_5)) 
  current_y_5 = int(get_pos_x_as_integer(unit_id_5))  

  courier1 = Courier(start_x_1, start_y_1, end_x_1, end_y_1, current_x_1, current_y_1)
  courier2 = Courier(start_x_2, start_y_2, end_x_2, end_y_2, current_x_2, current_y_2)
  courier3 = Courier(start_x_3, start_y_3, end_x_3, end_y_3, current_x_3, current_y_3)
  courier4 = Courier(start_x_4, start_y_4, end_x_4, end_y_4, current_x_4, current_y_4)
  courier5 = Courier(start_x_5, start_y_5, end_x_5, end_y_5, current_x_5, current_y_5)

  courier1_score = evaluate_courier_performance(courier1)
  courier2_score = evaluate_courier_performance(courier2)
  courier3_score = evaluate_courier_performance(courier3)
  courier4_score = evaluate_courier_performance(courier4)
  courier5_score = evaluate_courier_performance(courier5)

  courier1_score = int(courier1_score * 100)
  courier2_score = int(courier2_score * 100)
  courier3_score = int(courier3_score * 100)
  courier4_score = int(courier4_score * 100)
  courier5_score = int(courier5_score * 100)

  print("Unit_id:", unit_id_1)
  print("Courier_Score:", courier1_score)
  print("\n")
  print("Unit_id:", unit_id_2)
  print("Courier_Score:", courier2_score)
  print("\n")
  print("Unit_id:", unit_id_3)
  print("Courier_Score:", courier3_score)
  print("\n")
  print("Unit_id:", unit_id_4)
  print("Courier_Score:", courier4_score)
  print("\n")
  print("Unit_id:", unit_id_5)
  print("Courier_Score:", courier5_score)
  print("\n")

  data = {"task_id": task_id_1, "unit_id": "1", "score": courier1_score}
  response_request = requests.post("http://172.20.10.3:5000/score", json = data)
  request_data = response_request.json

  data = {"task_id": task_id_2, "unit_id": "2", "score": courier2_score}
  response_request = requests.post("http://172.20.10.3:5000/score", json = data)
  request_data = response_request.json

  data = {"task_id": task_id_3, "unit_id": "3", "score": courier3_score}
  response_request = requests.post("http://172.20.10.3:5000/score", json = data)
  request_data = response_request.json

  data = {"task_id": task_id_4, "unit_id": "4", "score": courier4_score}
  response_request = requests.post("http://172.20.10.3:5000/score", json = data)
  request_data = response_request.json

  data = {"task_id": task_id_5, "unit_id": "5", "score": courier5_score}
  response_request = requests.post("http://172.20.10.3:5000/score", json = data)
  request_data = response_request.json

  print(request_data)

  time.sleep(0.1)
