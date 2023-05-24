"""
zip - Unindo iteráveis so une ate a menor lista
zip_longest - Itertools
"""
### Código
from itertools import zip_longest, count

""" junta as cidade com o estado
cidades_estados = zip(cidades, estados)
print(list(cidades_estados))
print(dict(cidades_estados))
"""
"""junta as cidade com o estado
for valor in cidades_estados:
    print(valor)
"""
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(indice, cidades, estados)
#print(list(cidades_estados))
for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
