import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, False)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, False)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moedas.reduzir(p, 13, True)}')
