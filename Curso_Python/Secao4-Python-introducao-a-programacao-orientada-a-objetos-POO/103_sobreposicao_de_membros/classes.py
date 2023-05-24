class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} Comprando...')

    def falar(self):
        print(f'estou em cliente')


class ClienteVip(Cliente):
    # def falar(self):
    #     Pessoa.falar(self)
    #     Cliente.falar(self)
    #     print('\nVip falando')
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')
