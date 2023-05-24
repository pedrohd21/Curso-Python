produto = barato = n = 'e'
preco = total = maior = 0
menor = 9999
titulo = 'SUPERMERCADOS BH'
print('-' * 45)
print(titulo.center(45))
print('-' * 45)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco do produto: R$ '))
    total += preco
    if preco > 1000:
        maior += 1
    if preco < menor:
        menor = preco
        barato = produto
    n = str(input('Deseja continuar? [S/N] ')).upper()
    if n == 'N':
        break
print('-' * 15, end='')
print('Fim Programa')
print(f'Total da compra é R$ {total:.2f}\n{maior} produtos foram mais de R$ 1000,00\nE o produto mais barato é {barato}')
print('Volte sempre')
