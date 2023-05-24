n = 0
print('------Campeonato Brasileiro------')
classificação = ('Cruzeiro', 'São Paulo', 'Internacional', 'Corinthians', 'Atletico-Mg', 'Fluminense', 'Grêmio', 'Athletico-Pr', 'Santos', 'Flamengo', 'Sport Recife', 'Goias', 'Figueirense', 'Coritiba', 'Chapecoense', 'Palmeiras', 'EC Vitoria','Bahia', 'Botafogo', 'Criciúma')
for c in classificação:
    n += 1
    print(f'{n}° {c}')
print('-' * 100)
print(f'Classificados Libertadores: {classificação[0:5]}')
print('-'* 100)
print(f'A posição da Chapecoense é {classificação.index("Chapecoense")+ 1}°')
print('-'* 100)
print(f'Rebaixados {classificação[16:]}')
print('-'* 280)
print(f'Ordem Alfabetica {sorted(classificação)}')
