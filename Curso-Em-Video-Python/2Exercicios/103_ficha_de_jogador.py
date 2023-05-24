def jogador(nome='Desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato.')


#Programa principal
nome = str(input('Nome do jogador: '))
gols = str(input('Quantos gols marcou: '))
if len(nome) > 0:
    if gols.isnumeric() > 0:
        jogador(nome, int(gols))
    else:
        jogador(nome=nome)
if gols.isnumeric() > 0:
    if len(nome) == 0:
        if gols.isnumeric() > 0:
            jogador(gols=int(gols))
else:
    jogador()
