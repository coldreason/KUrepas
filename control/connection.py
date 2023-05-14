import requests

def connection_in(query, data=None):
    json_string = requests.get(query,json=data)
    if(len(json_string.text) == 3):
        return None
    return json_string

def connection_out(query, data):
    requests.post(query, json=data)
    return 0