"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

DUMPS / Dump converte para json
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load converte para python
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""

from dados import *
import json

# lista = [1, 2, 3, 4, 5, 6]
# dados_json = json.dumps(lista)
# print(type(dados_jason))

# dados_json = json.dumps(clientes_dicionario, indent=4)
# print(dados_json)


# dicionario = json.loads(clientes_json)
# for key, values in dicionario.items():
#     print(key)
#     print(values)

# escreve um arquivo
# with open('clientes.json', 'w') as arquivo:
#     json.dump(clientes_dicionario, arquivo, indent=4)

# transforma o arquivo em python
with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

for k, v in dados.items():
    print(k, '\n', v)
