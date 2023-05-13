import requests

def connection_in(query):
    json_string = requests.get(query)
    if(json_string == ''):
        return None
    return json_string

def connection_out(query, data):
    requests.post(query, json=data)
    return 0