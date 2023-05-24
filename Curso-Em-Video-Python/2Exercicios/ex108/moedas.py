def metade(valor=0):
    return valor / 2


def dobro(valor=0):
    return valor * 2


def aumentar(valor=0, porcento=0):
    aumento = valor + (valor * porcento / 100)
    return aumento


def reduzir(valor=0, porcento=0):
    reduz = valor - (valor * porcento / 100)
    return reduz

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
