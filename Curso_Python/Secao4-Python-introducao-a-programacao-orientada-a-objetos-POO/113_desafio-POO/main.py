from contas.corrente import Corrente
from contas.poupanca import Poupanca


p1 = Corrente('Pedro', 23, 500, 1234)
p1.depositar(100)
p1.sacar(200)
p1.detalhes()
print()


p2 = Corrente('Maria', 23, 1000, 1234)
p2.depositar(500)
p2.sacar(1200)
p2.detalhes()
print()


p3 = Corrente('Antonio', 23, 10, 1234)
p3.depositar(0)
p3.sacar(100)
p3.detalhes()
print()


p4 = Poupanca('Luana', 23, 600, 1234)
p4.depositar(100)
p4.sacar(800)
p4.detalhes()
print()


p5 = Poupanca('Juliana', 23, 5000, 1234)
p5.depositar(5000)
p5.sacar(7000)
p5.detalhes()
print()


p6 = Poupanca('Maria', 23, 0, 1234)
p6.depositar(100)
p6.sacar(200)
p6.detalhes()
print()


