from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.getter
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @idade.getter
    def idade(self):
        return self._idade


class Bank(ABC, Cliente):
    def __init__(self, nome, idade, saldo, numero, limite=0):
        self.saldo = saldo
        self.numero = numero
        self._limite = limite
        super().__init__(nome, idade)

    @property
    def limite(self):
        return self._limite

    @limite.getter
    def limite(self):
        return self._limite

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    def detalhes(self):
        print()
        print('Detalhes da Conta')
        print('-'*25)
        print(f'Agencia: {self.numero}')
        print(f'Conta Usuario: {self.nome}')
        print(f'Saldo Atual: {self.saldo}')
        data_abertura = datetime.today().strftime('Dia %d/%m/%Y Horas %H:%M')
        print(f'Transação {data_abertura}')
        print('-'*25)




