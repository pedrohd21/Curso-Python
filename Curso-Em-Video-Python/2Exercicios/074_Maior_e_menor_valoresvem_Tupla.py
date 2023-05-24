from random import randint
numero = (randint(0, 30), randint(0, 30), randint(0, 30), randint(0, 30), randint(0, 30))
print(' Os numeros sorteados foram: ', end='')
for n in numero:
    print(f'{n}', end=' ')
print(f'\n Maior numero: {max(numero)}\n Menor numero: {min(numero)}')
