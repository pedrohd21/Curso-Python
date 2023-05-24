''' Exemplo 1
c = 1
while c < 11:
    print(c)
    c += 1
print('Fim')
'''
'''eXEMPLO 2 
n = 1
while n!= 0:
    n = int(input('Digite um valor: '))
print('Fim') '''
''' Exemplo 3
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''
''' Exemplo 4
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par +=1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares!'.format(par, impar))'''
'''Exemplo 5
from random import randint
computador = randint(1, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez')
print('Acertou com {} tentativas. Parabens!!'.format(palpites))'''

n = int(input('digite um numero:'))
c = 0
while c < 5:
    c += 1
    print('Menor ' if n < 3 else 'Maior')