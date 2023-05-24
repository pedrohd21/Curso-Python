"""
split, join, enumerate em python
* Split - Dividir uma string # str
* join - Juntar uma lista #str
* enumerate - enumerar elementos da lista # Iteraveis
"""
string = 'O Brasil é penta.'
lista = string.split(' ') #todo: split separa cada palavra em uma lista
lista1 = ','.join(lista) #todo: join junta uma lista
print(string)
print(lista)
print(lista1)

print('enumerate')
for indice, valor in enumerate(lista):
    print(indice, valor)

lista2 = [
    ['Codigo', 'Produto', 'Preço'],
    ['01', 'Celular', 'R$ 4.500,00'],
    ['02', 'Camera', 'R$ 2.100,00'],
]
for v in lista2:
    print(f"{v[0]:^6} {v[1]:^10} {v[2]:^10}")
