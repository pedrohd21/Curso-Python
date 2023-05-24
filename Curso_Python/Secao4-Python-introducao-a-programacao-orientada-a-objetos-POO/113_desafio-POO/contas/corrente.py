from contas.conta import Bank


class Corrente(Bank):
    def __init__(self, nome, idade, saldo, numero, limite=200):
        super().__init__(nome, idade, saldo, numero, limite)

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do deposito precisa ser numerico.')

        self.saldo += valor
        print(f'Conta: {self.numero}, Usuario {self.nome}, Depositando: R$ {valor}')

    def sacar(self, valor):
        if valor <= self.limite:
            self.saldo -= valor
            print(f'Conta: {self.numero}, Usuario {self.nome} Sacando: R$ {valor}')
        else:
            print(f'Conta: {self.numero}, Usuario {self.nome} no momento sem limite de saque')
