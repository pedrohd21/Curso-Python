'''
from random import randint
from time import sleep
from operator import itemgetter
dado = {'jogador1': randint(0, 6),
        'jogador2': randint(0, 6),
        'jogador3': randint(0, 6),
        'jogador4': randint(0, 6)}
ranking = list()
print('=-'*12)
print(f'{"valores sorteados":^24}')
print('=-'*12)
for c, i in dado.items():
    print(f'O {c} tirou {i} no dado')
    sleep(1)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('=-'*12)
print(f'{"==== Ranking ====":^24}')
print('=-'*12)
for c, i in enumerate(ranking):
    print(f'{c + 1}° Lugar: {i[0]} com {i[1]}')
    sleep(1)
'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-' * 30)
print('  == RANKING DO JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i + 1}° lugar {v[0]} com {v[1]}.')
    sleep(1)
