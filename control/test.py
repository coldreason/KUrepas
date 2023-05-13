import json
from connection_test import connection_in, connection_out
import threading
import random

json_string_in = connection_in()
json_object_in = json.loads(json_string_in) # dict type
print(json_object_in)



json_object_out = {'id': 1, 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874'}, 'admin': False, 'hobbies': None}
connection_out(json_object_out)

taskSet = [] # dict list
print()
print()
taskSet.append({'id': 1, 'username': 'Bret', 'email': 'Sincere@april.biz'}) # Initialize
taskSet.append({'id': 1, 'username': 'Bret', 'email': 'Sincere@april.biz'})
print(taskSet)
print(len(taskSet))
hi = []
print(hi)
print(len(hi))
def ppp5(i):
	print('hello0.5' + i)
	threading.Timer(0.5, ppp5).start()
def ppp11():
	print('hello1.1')
	threading.Timer(1.1, ppp11).start()

ppp5(6)
ppp11()