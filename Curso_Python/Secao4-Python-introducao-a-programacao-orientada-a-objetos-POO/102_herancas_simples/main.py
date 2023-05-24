from classes import Cliente, Aluno

"""
Associação - Usa | Agregação - Tem | Composição - É dono | Heranca - É
"""
c1 = Cliente('Pedro', 23)
# print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 25)
# print(a1.nome)
a1.falar()
a1.estudar()

teste = Cliente('pedro', 25)

print(teste.nome, teste.idade)
