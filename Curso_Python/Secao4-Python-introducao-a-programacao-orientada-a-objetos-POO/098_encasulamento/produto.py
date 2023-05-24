class Produto:
    def __init__(self, nome, preco=0, quantidade=0):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco
    
    
    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
    
    
    def valorTotalEstoque(self):
        return self.__preco * self.__quantidade
    
    
    def addProdutos(self, quantidade):
        self.__quantidade += quantidade
        
    
    def removerProdutos(self, quantidade):
        self.__quantidade -= quantidade