import json
import requests
import torch
import torch.nn as nn
import random
import time
import numpy as np

current_pos_x_1 = random.randint(0,20)
current_pos_y_1 = random.randint(0,20)
current_pos_x_2 = random.randint(0,20)
current_pos_y_2 = random.randint(0,20)
current_pos_x_3 = random.randint(0,20)
current_pos_y_3 = random.randint(0,20)
current_pos_x_4 = random.randint(0,20)
current_pos_y_4 = random.randint(0,20)
current_pos_x_5 = random.randint(0,20)
current_pos_y_5 = random.randint(0,20)

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

    return score.item()

class Courier:
    def __init__(self, start_x, start_y, end_x, end_y, current_x, current_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.current_x = current_x
        self.current_y = current_y
  courier1 = Courier(random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20))
  courier2 = Courier(random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20))
  courier3 = Courier(random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20))
  courier4 = Courier(random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20))
  courier5 = Courier(random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20))
  
    inputs = torch.tensor([
        [courier.start_x, courier.start_y, courier.end_x, 
         courier.end_y, courier.current_x, courier.current_y]
    ], dtype=torch.float)

    score = model(inputs)
while True:
  enable = [0,0,0,0,0]
  print('만약 get을 했는데 taskid가 변하지 않았다면 continue')
  get_taskid = requests.post("http://172.20.10.3:5000/score_request", json = data)
  taskid = get_taskid.json
  
  if task_id != taskid:
    continue
    
  print('score request로부터 taskid가 바뀌기 직전까지 taskid, unitid 읽고enable[i]=1 로 처리')
  while taskid[i] != taskid[i+1]:
    taskid = task_id
    unitid = unit_id
    enable[i] == 1
    
  if(enable[i] == 1):
    courier1 = Courier(random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20))
    courier1_score = int(evaluate_courier_performance(courier1)* 100 % 100)
    response_request = requests.post("http://172.20.10.3:5000/score", json = {"task_id": task_id, "unit_id": 1, "score": courier1_score})
  if(enable[i] == 1):
    courier2 = Courier(random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20))
    courier2_score = int(evaluate_courier_performance(courier2)* 100 % 100)
    response_request = requests.post("http://172.20.10.3:5000/score", json = {"task_id": task_id, "unit_id": 2, "score": courier1_score})
  if(enable[i] == 1):
    courier3 = Courier(random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20))
    courier3_score = int(evaluate_courier_performance(courier3)* 100 % 100)
    response_request = requests.post("http://172.20.10.3:5000/score", json = {"task_id": task_id, "unit_id": 3, "score": courier1_score})
  if(enable[i] == 1):
    courier4 = Courier(random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20))
    courier4_score = int(evaluate_courier_performance(courier4)* 100 % 100)
    response_request = requests.post("http://172.20.10.3:5000/score", json = {"task_id": task_id, "unit_id": 4, "score": courier1_score})
  if(enable[i] == 1):
    courier5 = Courier(random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20))
    courier5_score = int(evaluate_courier_performance(courier5)* 100 % 100)
    response_request = requests.post("http://172.20.10.3:5000/score", json = {"task_id": task_id, "unit_id": 5, "score": courier1_score})

  time.sleep(0.1)
