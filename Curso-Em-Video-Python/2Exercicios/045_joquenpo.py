from random import randint
from time import sleep
nome = str(input('Digite Seu nome: '))
jogador = int(input('''[0] Pedra
[1] Papel 
[2] Tesoura
Escolha uma opção: '''))
jogada0 = ('Pedra Papel Tesoura').split()
pc = randint(1, 2)
print('-' * 30)
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
sleep(1)
print('{} Jogou {}'.format(nome, jogada0[jogador]))
print('PC Jogou {}'.format(jogada0[pc]))
if pc == 1: #Pedra
    if jogador == 1:#pedra
        print('Empate!!')
    elif jogador == 2:#papel
        print('{} Venceu!!'.format(nome))
    elif jogador == 3:#tesou
        print('Pc Venceu!!')
elif pc == 2: #papel
    if jogador == 1: #pedr
        print('Pc Venceu!!')
    elif jogador == 2:#papel
        print('Empate!!')
    elif jogador == 3: #teso
        print('{} Venceu!!'.format(nome))
elif pc == 3: #tesoura
    if jogador == 1:#pedra
        print('{} Venceu!!'.format(nome))
    elif jogador == 2:#papel
        print('Pc Venceu!!')
    elif jogador == 3:#tesou
        print('Empate!!')
else:
    print('Opção invalida')