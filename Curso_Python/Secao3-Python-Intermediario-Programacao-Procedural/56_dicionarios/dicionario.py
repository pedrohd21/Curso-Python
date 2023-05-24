"""
Dicionários
"""
"""
parte 1
dicionario = {1: 'Valor 1', 2: 'Valor 2', 3: 'Valor3'}
dicionario['str'] = 'valor'
dicionario['1'] = 'Agora existe'
if dicionario.get('str') is not None:  # Retorna um valor none, mas como existe nn retorna um valor None
    print(dicionario.get('str'))
print(dicionario)
del dicionario['1']  # Apaga valor
print(dicionario)
print('str' in dicionario)  # Retorna um valor Booleano
print(len(dicionario))
for k in dicionario.items():  # mostra o dicionário completo .items
    print(k[0], k[1])
for k, v in dicionario.items():
    print(k, v)
"""

""" Parte 2
clientes = {'cliente1': {'nome': 'Luiz', 'sobrenome': 'Ótavio'},
            'cliente2': {'nome': 'João', 'sobrenome': 'Moreira'}}
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
"""

""" parte 3 cria uma copia raza
#  a copy pode acabar nn sendo muito util, pois dependendo da situação o valor do dicionario vai mudar junto com o outro
d1 = {1: 'a', 2: 'b', 3: 'c', 4: ['Luiz', 'Otavio']}
v = d1.copy()

v[1] = 'Luiz'
v[4][0] = 'Joãozinho'
print(d1)
print(v)
"""
"""
# Cria uma copia de vdd, nn muda as duas em hipotese nenhuma
import copy
d1 = {1: 'a', 2: 'b', 3: 'c', 4: ['Luiz', 'Otavio']}
v = copy.deepcopy(d1)

v[1] = 'Luiz'
v[4][0] = 'Joãozinho'
print(d1)
print(v)
"""

d1 = {1: 1, 2: 2, 3: 3}
d1.pop(3)  # Apaga o valor desejado da lista
d1.popitem()  # Apaga o ultimo valor da lista
print(d1)
d2 = {4: 4, 5: 5, 6: 6, 7: 7}
d1.update(d2)  # Junta a outra dicionario na d1
print(d1)