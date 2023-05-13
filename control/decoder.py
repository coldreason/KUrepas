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
		print(New_data['unitID'])
		print(New_data['min_x'])
		print(New_data['max_x'])
		print(New_data['min_y'])
		print(New_data['max_y'])
		print(New_object_in)
		return New_object_in

def decoder_scoreQueue():
	New_data = connection_in() #json
	if(New_data == None):
		print('no new task detected in Queue')
	else:
		New_object_in = json.loads(New_data) # dict
		print('new task detected')
		print(New_data['taskID'])
		print(New_data['unitID'])
		print(New_data['score'])
		print(New_object_in)
		return New_object_in