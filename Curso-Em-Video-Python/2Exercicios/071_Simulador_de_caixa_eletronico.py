titulo = 'BANC Actuli'
print('='*40)
print(titulo.center(40))
print('='*40)
saque = int(input('Qual o valor a sacar? R$'))
n = nota = nota1 = nota20 = nota50 = nota10 = 0
while n < 2:
    if saque >= 50:
        nota= saque // 50
        nota50 += 1
        saque -= 50
    elif saque >= 20:
        nota = saque // 20
        nota20 += 1
        saque -= 20
    elif saque >= 10:
        nota = saque // 10
        nota10 += 1
        saque -= 10
    else:
        nota = saque // 1
        saque -= 1
        nota1 += 1
    if saque == 0:
        break
print(f'Total de {nota50} cédulas de R$ 50')
print(f'Total de {nota20} cédulas de R$ 20')
print(f'Total de {nota10} cédulas de R$ 10')
print(f'Total de {nota1} cédulas de R$ 1')
print('='*40)
print('Volte Sempre ao Banc Actuali!!')

