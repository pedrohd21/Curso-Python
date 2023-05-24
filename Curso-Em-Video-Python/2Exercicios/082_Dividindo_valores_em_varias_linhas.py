c = 's'
par = []
impar = []
juntas = []
while c != 'N':
    valor = int(input('Digite um numero: '))
    c = str(input('Quer continuar? [S/N]')).upper()
    juntas.append(valor)
    if c == 'S':
        print('', end='')
    elif c == 'N':
        c = 'N'
    else:
        print('Opção invalida')
for c, valor in enumerate(juntas):
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'Lista completa é {juntas}')
print(f'Lista de pares é {par}')
print(f'Lista de impares é {impar}')