from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando os 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print('Pronto!')


def par(lista):
    print(f'Somando os valores pares de {lista}', end='')
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f', temos {soma}')


numero = list()
sorteia(numero)
par(numero)
