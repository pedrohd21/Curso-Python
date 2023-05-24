class Banco:
    def __init__(self, numero, nome, saldo=0):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
        
    
    @property
    def numero(self):
        return self.__numero
    
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def saldo(self):
        return self.__saldo

    def deposito(self, deposito):
        self.__saldo += deposito
    
    def saque(self, saque):
        self.__saldo -= saque + 5