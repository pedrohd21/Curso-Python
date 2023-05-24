lista = ('Lapis', 1.70,
         'Borracha', 2,
         'Caderno', 10.40,
         'Mochila', 80.76,
         'Caneta', 1.50)
print(f'{"Lista de Preços":^28}')
for n in range(0, len(lista)):
    if n % 2 == 0:
        print(f'{lista[n]:.<20}', end='')
    else:
        print(f'{lista[n]:>7.2f}')
'''Sempre que precisar lembrar de uma lista aq estar'''
