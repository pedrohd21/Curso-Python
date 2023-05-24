from produto import Produto

p1 = Produto('Tv', 900, 100)

print(f'Valor total da {p1.nome} em estoque: R${p1.valorTotalEstoque():.2f}')

p1.addProdutos(10)
print(p1.quantidade)

p1.removerProdutos(15)
print(p1.quantidade)

p2 = Produto('notevf', 1200)
print(p2.quantidade)
p2.addProdutos(10)
print(p2.quantidade)