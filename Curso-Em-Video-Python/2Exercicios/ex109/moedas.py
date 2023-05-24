def metade(valor=0, formato=False):
    resp = valor / 2
    return resp if formato is False else moeda(resp)


def dobro(valor=0, formato=False):
    resp = valor * 2
    return resp if formato is False else moeda(resp)


def aumentar(valor=0, porcento=0, formato=False):
    aumento = valor + (valor * porcento / 100)
    return aumento if formato is False else moeda(aumento)


def reduzir(valor=0, porcento=0, formato=False):
    reduz = valor - (valor * porcento / 100)
    return reduz if formato is False else moeda(reduz)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
