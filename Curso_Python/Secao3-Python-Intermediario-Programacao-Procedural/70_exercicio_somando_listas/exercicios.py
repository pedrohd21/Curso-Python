"""
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4]
if lista1 < lista2:
    for k, v in enumerate(lista1):
        soma = 0
        soma = v + lista2[k]
        print(soma, end=" ")
else:
    for k, v in enumerate(lista2):
        soma = 0
        soma += v + lista1[k]
        print(soma, end=" ")
"""

lista1 = [1, 18, 3, 4, 5]
lista2 = [1, 2, 3, 4]
soma = [x + y for x, y in zip(lista1, lista2)]
print(soma)
