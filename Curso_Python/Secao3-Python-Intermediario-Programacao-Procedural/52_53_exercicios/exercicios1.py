numero = input('Digite um numero: ')


def func1(valor):
    func2(valor)


def func2(valor):
    print(valor)


result = func1(numero)

