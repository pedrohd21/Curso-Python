class Estoque():
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def total(self):
        return self.preco * self.quantidade

    def adicionar(self, valor):
        self.quantidade += valor
        
    def remover(self, valor):
        self.quantidade -= valor