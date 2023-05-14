import json
from connection import connection_in

def decoder_taskQueue():
    New_data = connection_in('http://172.20.10.3:5000/taskqueue') # json
    if(New_data == None):
        return None
    else:
        New_object_in = New_data.json() # dict
        return New_object_in

def decoder_scoreQueue(taskID, unitID): # task = 7 unit - 0, 1, 4
    New_data = connection_in('http://172.20.10.3:5000/score',data={"task_id":str(taskID), "unit_id":str(unitID)}) #json
    if(New_data == None):
        return None
    else:
        New_object_in = New_data.json() # dict
        return New_object_in

# def decoder_designateQueue():
#     New_data = connection_in('http://54.180.109.46:5000/designatequeue') #json
#     if(New_data == None):
#         return None
#     else:
#         New_object_in = New_data.json() # dict
#         return New_object_in