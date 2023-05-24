from estoque import Estoque

# nome = input('Nome do produto: ')
# preco = float(input('Preco do produto: R$ '))
# quantidade = int(input('Quantidade de produtos: '))


p1 = Estoque('Tv', 50, 10)

p1.adicionar(10)
p1.remover(5)
print(f'Produto inicial: Produto: {p1.nome}, R${p1.preco}, Quantidade: {p1.quantidade}')
print('Total', p1.total())