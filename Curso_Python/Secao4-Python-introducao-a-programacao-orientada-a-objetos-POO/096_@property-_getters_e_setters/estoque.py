class Estoque:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    
    def totalEstoque(self):
        return self.preco * self.quantidade
    
    
    def adicionar(self, add):
        self.quantidade += add
    
    
    def remover(self, remover):
        self.quantidade -= remover


print('Produto')
nome = input('Nome: ')
preco = float(input('Preco: R$'))
quantidade = int(input('Quantidade em estoque: '))

produto = Estoque(nome, preco, quantidade)

produto.adicionar(10)
produto.remover(5)
print(produto.quantidade)