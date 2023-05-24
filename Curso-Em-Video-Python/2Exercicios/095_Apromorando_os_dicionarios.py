
jogadores = dict()
gol = list()
dados = list()
while True:
    gol.clear()
    jogadores['nome'] = str(input('Nome do jogador: '))
    jogadores['partidas'] = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))

    for c in range(0, jogadores['partidas']):
        gol.append(int(input(f'   Quantos gols na partida {c + 1}: ')))
    jogadores['gols'] = gol[:]
    dados.append(jogadores.copy())

    while True:
        cont = str(input('Quer continuar: [S/N] ')).upper()[0]
        if cont in 'SN':
            break
        print('Error!!')

    if cont == 'N':
        break

print(f'{"cod nome":<22} {"gols":<18} {"total"}')
print('-'*50)
for c, i in enumerate(dados):
    print(f'  {c} {(i["nome"]):<18} {str(i["gols"]):<18} {sum(i["gols"])}')

while True:
    cont = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cont == 999:
        break
    elif cont >= len(dados):
        print(f'Erro! Não existe jogador com o codigo {cont}!')
    else:
        print(f' --LEVANTAMENTO DO JOGADOR {dados[cont]["nome"]}:')
        for c, v in enumerate(dados[cont]['gols']):
            print(f'   No jogo {c + 1} fez {v} gols.')

'''
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador? '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro!! Responda apenas S ou N.')
    if resp == 'N':
        break
print('=-'* 30)
print('Cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de quel jogador? (999 para parar) '))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'Erro!! Não existe jogador com codigo {busca}')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-'*30)
print('<<VOLTE SEMPRE')
'''