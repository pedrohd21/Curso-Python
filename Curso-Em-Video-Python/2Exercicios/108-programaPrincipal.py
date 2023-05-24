from ex108 import moedas

preço = float(input('Digite o preço: R$ '))
print(f'A metade de {preço} é {moedas.metade(preço):.2f}')
print(f'O dobro de {preço} é {moedas.dobro(preço):.2f}')
print(f'Aumentando 10%, temos {moedas.aumentar(preço, 10):.2f}')
print(f'Reduzindo 13%, temos {moedas.reduzir(preço, 13):.2f}')