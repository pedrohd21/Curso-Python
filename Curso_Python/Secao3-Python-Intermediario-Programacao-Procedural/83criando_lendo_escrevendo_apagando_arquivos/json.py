import json

d1 = {'Pessoa 1': {'nome': 'Pedro', 'idade': 23}, 'Pessoa 2': {'nome': 'João', 'idade': 40}}

d1_json = dumps(d1, indent=True)
print(d1_json)
