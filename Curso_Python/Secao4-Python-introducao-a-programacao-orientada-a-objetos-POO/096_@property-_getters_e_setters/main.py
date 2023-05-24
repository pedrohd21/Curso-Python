class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcentual):
        self.preco = self.preco - (self.preco * (porcentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, preco):
        self._nome = preco.upper()

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, preco):
        if isinstance(preco, str):
            preco = float(preco.replace('R$', ''))
        self._preco = preco


p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)

