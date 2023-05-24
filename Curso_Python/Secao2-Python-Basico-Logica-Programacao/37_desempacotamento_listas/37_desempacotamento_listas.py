"""
Desempacotamento de listas em python
"""
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5]
n1, n2, *n3 = lista #todo: usando a * cria outra lista, e os valores que eu quiser mostrar, começa pelas ultimas
print(n3)
