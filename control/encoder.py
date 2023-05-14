import json
from connection import connection_out

def encoder_taskSet(i,writeData):
    object_out = json.dumps(writeData)
    connection_out('http://172.20.10.3:5000/refreshMap', {"id":i,"map":object_out})
    
def encoder_requestQueue(writeData):
    object_out = json.dumps(writeData)
    print(object_out)
    connection_out('http://172.20.10.3:5000/score_request', object_out)
    
def encoder_designateQueue(writeData):
    object_out = json.dumps(writeData)
    print(object_out)
    connection_out('http://172.20.10.3:5000/designate', object_out)