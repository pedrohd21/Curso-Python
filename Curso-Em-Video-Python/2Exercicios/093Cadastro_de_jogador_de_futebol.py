'''
dados = dict()
gol = list()
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, partidas):
    gol.append(int(input(f'Quantos gols na partida {c}? ')))
dados['gols'] = gol[:]
dados['total'] = sum(gol)
print('=-'*26)
print(dados)
print('=-'*26)
print(f'Nome do Jogador: {dados["nome"]}')
print(f'Gols por partida: {dados["gols"]}')
print(f'O total de gol é: {dados["total"]}')
print('=-'*26)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'   => Na partida {c}, fez {dados["gols"][c]} gols')
print(f'Foi um total de {dados["total"]} gols')
'''
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'   => na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')
