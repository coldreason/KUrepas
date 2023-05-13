import json
from connection import connection_out

def encoder_taskSet(writeData):
	print('taskSet new allocated')
	print(writeData['unitID'])
	print(writeData['min_x'])
	print(writeData['max_x'])
	print(writeData['min_y'])
	print(writeData['max_y'])
	object_out = json.dumps(writeData)
	connection_out(object_out)
	return 0
	
def encoder_requestQueue(writeData):
	print('request updated')
	print(writeData['unitID'])
	print(writeData['taskID'])
	object_out = json.dumps(writeData)
	connection_out(object_out)
	return 0
	
def encoder_designateQueue(writeData):
	print('designate updated')
	print(writeData['taskID'])
	print(writeData['unitID'])
	print(writeData['score'])
	print(writeData['complete'])
	object_out = json.dumps(writeData)
	connection_out(object_out)
	return 0