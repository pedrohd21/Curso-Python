from random import sample
mega = []
print(f'{"Mega Sena":^35}')
print('='*35)
jogos = int(input('Quantos jogos seram jogados? '))
print(f'{"-"}'*35)

for c in range(0, jogos):
    mega.append(sample(range(1, 60), 6))

for c in range(0, jogos):
        mega[c].sort()

for c in range(0, jogos):
    print(f'Jogo {c + 1}: ', end=' ')
    for i in range(0, 1):
        print(mega[c])
print('='*35)
print(f'{"Boa Sorte":^35}')
