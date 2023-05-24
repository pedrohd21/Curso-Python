from contas.conta import Bank


class Poupanca(Bank):
    def __init__(self, nome, idade, saldo, numero, limite=0):
        super().__init__(nome, idade, saldo, numero, limite)

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do deposito precisa ser numerico.')

        self.saldo += valor
        print(f'Conta: {self.numero}, Usuario {self.nome} Depositando: R$ {valor}')
        print()

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Conta: {self.numero}, Usuario {self.nome} Sacando: R$ {valor}')
            print()
        else:
            print(f'Conta: {self.numero}, Usuario {self.nome} no momento sem limite de saque')