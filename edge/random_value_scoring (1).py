# -*- coding: utf-8 -*-
"""Random_value_scoring.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NBklXHYkoLS145pwd5xoPFc5A7470Exf
"""

import torch
import torch.nn as nn
import random

def get_random_float(start, end):
    return round(random.uniform(start, end), 1)

def get_random_integer(start, end):
    return random.randint(start, end)

class PerformanceEvaluator(nn.Module):
    def __init__(self):
        super(PerformanceEvaluator, self).__init__()
        self.conv = nn.Conv1d(5, 16, kernel_size=1)
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
        [courier.delivery_speed, courier.average_speed, courier.average_rating, 
         courier.completed_orders, courier.total_orders]
    ], dtype=torch.float)

    score = model(inputs)

    return score.item()

class Courier:
    def __init__(self, delivery_speed, average_speed, average_rating, completed_orders, total_orders):
        self.delivery_speed = delivery_speed
        self.average_speed = average_speed
        self.average_rating = average_rating
        self.completed_orders = completed_orders
        self.total_orders = total_orders

delivery_speed_1 = get_random_integer(5, 15)
delivery_speed_2 = get_random_integer(5, 15)
delivery_speed_3 = get_random_integer(5, 15)
delivery_speed_4 = get_random_integer(5, 15)
delivery_speed_5 = get_random_integer(5, 15)

average_speed_1 = get_random_integer(5, 15)
average_speed_2 = get_random_integer(5, 15)
average_speed_3 = get_random_integer(5, 15)
average_speed_4 = get_random_integer(5, 15)
average_speed_5 = get_random_integer(5, 15)

average_rating_1 = get_random_float(3.0, 5.0)
average_rating_2 = get_random_float(3.0, 5.0)
average_rating_3 = get_random_float(3.0, 5.0)
average_rating_4 = get_random_float(3.0, 5.0)
average_rating_5 = get_random_float(3.0, 5.0)

completed_orders_1 = get_random_integer(180, 230)
completed_orders_2 = get_random_integer(180, 230)
completed_orders_3 = get_random_integer(180, 230)
completed_orders_4 = get_random_integer(180, 230)
completed_orders_5 = get_random_integer(180, 230)

total_orders_1 = get_random_integer(completed_orders_1, 230)
total_orders_2 = get_random_integer(completed_orders_2, 230)
total_orders_3 = get_random_integer(completed_orders_3, 230)
total_orders_4 = get_random_integer(completed_orders_3, 230)
total_orders_5 = get_random_integer(completed_orders_3, 230)

courier1 = Courier(delivery_speed_1, average_speed_1, average_rating_1, completed_orders_1, total_orders_1)
courier2 = Courier(delivery_speed_2, average_speed_2, average_rating_2, completed_orders_2, total_orders_2)
courier3 = Courier(delivery_speed_3, average_speed_3, average_rating_3, completed_orders_3, total_orders_3)
courier4 = Courier(delivery_speed_4, average_speed_4, average_rating_4, completed_orders_4, total_orders_4)
courier5 = Courier(delivery_speed_5, average_speed_5, average_rating_5, completed_orders_5, total_orders_5)

courier1_score = evaluate_courier_performance(courier1)
courier2_score = evaluate_courier_performance(courier2)
courier3_score = evaluate_courier_performance(courier3)
courier4_score = evaluate_courier_performance(courier4)
courier5_score = evaluate_courier_performance(courier5)

print("Courier 1 Score:", courier1_score)
print("Courier 2 Score:", courier2_score)
print("Courier 3 Score:", courier3_score)
print("Courier 4 Score:", courier4_score)
print("Courier 5 Score:", courier5_score)

file_paths = ["performance_scores1.txt", "performance_scores2.txt", "performance_scores3.txt", "performance_scores4.txt", "performance_scores5.txt"]

for i, file_path in enumerate(file_paths):
    with open(file_path, "w") as file:
        file.write("Courier_Status =\n\n[speed / average speed / average rating / completed missions / total missions]\n\n")
        courier = None

        if i == 0:
            courier = courier1
            courier_score = courier1_score
        elif i == 1:
            courier = courier2
            courier_score = courier2_score
        elif i == 2:
            courier = courier3
            courier_score = courier3_score
        elif i == 3:
            courier = courier4
            courier_score = courier4_score
        elif i == 4:
            courier = courier5
            courier_score = courier5_score

        courier_values = [str(val) for val in [
            courier.delivery_speed, courier.average_speed, courier.average_rating,
            courier.completed_orders, courier.total_orders
        ]]
        file.write(f"Courier{i+1}_status = " + ", ".join(courier_values) + "\n")

        file.write(f"Courier {i+1} Score: {courier_score}\n")

    print(f"\nCourier {i+1}'s Status and Score have been written to {file_path}")