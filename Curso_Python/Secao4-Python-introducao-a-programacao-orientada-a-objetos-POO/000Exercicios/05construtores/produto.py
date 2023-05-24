class Produto:
    def __init__(self, nome, preco=0, quantidade=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    
    def valorTotalEstoque(self):
        return self.preco * self.quantidade
    
    
    def addProdutos(self, quantidade):
        self.quantidade += quantidade
        
    
    def removerProdutos(self, quantidade):
        self.quantidade -= quantidade