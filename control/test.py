import json
from connection_test import connection_in, connection_out

json_string_in = connection_in()
json_object_in = json.loads(json_string_in) # dict type
print(json_object_in)



json_object_out = {'id': 1, 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874'}, 'admin': False, 'hobbies': None}
connection_out(json_object_out)