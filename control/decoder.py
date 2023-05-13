import json
from connection import connection_in

def decoder_taskQueue():
	New_data = connection_in('http://54.180.109.46:5000/taskqueue/get_next') # json
	if(New_data == None):
		print('no new task detected in Queue')
		return None
	else:
		New_object_in = json.loads(New_data) # dict
		print('new task detected')
		print(New_object_in)
		return New_object_in

def decoder_scoreQueue():
	New_data = connection_in('http://54.180.109.46:5000/scorequeue/get_next') #json
	if(New_data == None):
		print('no new task detected in Queue')
		return None
	else:
		New_object_in = json.loads(New_data) # dict
		print('new task detected')
		print(New_object_in)
		return New_object_in

def decoder_designateQueue():
	New_data = connection_in('http://54.180.109.46:5000/designatequeue/get_next') #json
	if(New_data == None):
		print('no new complete signal detected in Queue')
		return None
	else:
		New_object_in = json.loads(New_data) # dict
		print('new complete signal detected')
		print(New_object_in['taskID'])
		print(New_object_in['unitID'])
		print(New_object_in['score'])
		print(New_object_in['complete'])
		return New_object_in