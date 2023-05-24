"""
count - itertools
"""
from itertools import count
# O contador count não tem fim
# O contador pra para num laço for usando um if com break

contador = count(start=9, step=-1)
# start onde começa a contar
# step para pular ex: 2, 4, 6, 8 e da pra usar pra contar ao contrario usando -1

for c in contador:
    print(round(c, 2))
    # round casas decimais
    if c >= 10 or c <= -10:
        break

print('#' * 20)
contador1 = count()
lista = ['Pedro', 'Henrique', 'Paula']
lista = zip(contador1, lista)
print(list(lista))
