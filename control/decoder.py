import json
from connection import connection_in

def decoder_taskQueue():
	New_data = connection_in() # json
	if(New_data == None):
		print('no new task detected in Queue')
	else:
		New_object_in = json.loads(New_data) # dict
		print('new task detected')
		print(New_data['pos_s_x'])
		print(New_data['pos_s_y'])
		print(New_data['pos_e_x'])
		print(New_data['pos_e_y'])
		print(New_object_in)
		return New_object_in
            
def decoder_taskSet():
	New_data = connection_in() #json
	if(New_data == None):
		print('no new task detected in Queue')
	else:
		New_object_in = json.loads(New_data) # dict
		print('new task detected')
		print(New_object_in['unitID'])
		print(New_object_in['min_x'])
		print(New_object_in['max_x'])
		print(New_object_in['min_y'])
		print(New_object_in['max_y'])
		return New_object_in

def decoder_scoreQueue():
	New_data = connection_in() #json
	if(New_data == None):
		print('no new task detected in Queue')
	else:
		New_object_in = json.loads(New_data) # dict
		print('new task detected')
		print(New_object_in['taskID'])
		print(New_object_in['unitID'])
		print(New_object_in['score'])
		return New_object_in

def decoder_designateQueue():
	New_data = connection_in() #json
	if(New_data == None):
		print('no new complete signal detected in Queue')
	else:
		New_object_in = json.loads(New_data) # dict
		print('new complete signal detected')
		print(New_object_in['taskID'])
		print(New_object_in['unitID'])
		print(New_object_in['score'])
		print(New_object_in['complete'])
		return New_object_in