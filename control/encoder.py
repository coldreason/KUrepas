import json
from connection import connection_out

def encoder_taskSet(writeData):
    print('taskSet new allocated')
    print(writeData)
    object_out = json.dumps(writeData)
    connection_out('http://54.180.109.46:5000/taskset', object_out)
    return 0
    
def encoder_requestQueue(writeData):
    print('request updated')
    print(writeData)
    object_out = json.dumps(writeData)
    connection_out('http://54.180.109.46:5000/requestqueue', object_out)
    return 0
    
def encoder_designateQueue(writeData):
    print('designate updated')
    print(writeData)
    object_out = json.dumps(writeData)
    connection_out('http://54.180.109.46:5000/designatequeue', object_out)
    return 0