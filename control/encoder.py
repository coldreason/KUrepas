import json
from connection import connection_out

def encoder_taskSet(i,writeData):
    object_out = json.dumps(writeData)
    connection_out('http://54.180.109.46:5000/refreshMap', {"id":i,"map":object_out})
    
def encoder_requestQueue(writeData):
    object_out = json.dumps(writeData)
    connection_out('http://54.180.109.46:5000/requestqueue', object_out)
    
def encoder_designateQueue(writeData):
    object_out = json.dumps(writeData)
    print('hello')
    print(object_out)
    connection_out('http://54.180.109.46:5000/designatequeue', object_out)