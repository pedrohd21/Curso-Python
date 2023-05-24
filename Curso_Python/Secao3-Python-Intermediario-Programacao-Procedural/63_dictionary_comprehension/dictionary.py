import sys
lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave1', 'valor1'),
]

#d1 = {x.upper(): y.upper() for x, y in lista} # deixa tudo em maiusculo
#d1 = {x for x in range(5)}
d1 = {f'chave_{x}': 'a' for x in range(5)}
print(d1)
print(sys.getsizeof(d1))
print(sys.getsizeof(lista))