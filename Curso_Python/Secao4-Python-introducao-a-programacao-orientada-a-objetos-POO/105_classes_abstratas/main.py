from classes.conta_poupanca import ContaPoupanca
from classes.conta_corrente import ContaCorrente


cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(5)

print('#' * 40)
cc = ContaCorrente(1111, 222, 0, 500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)
