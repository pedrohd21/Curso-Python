import re
import random


def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def total(lista):
    lista1 = '6543298765432'
    total1 = 0
    total2 = 0
    for c in range(11):
        total1 += int(lista[c]) * int(lista1[1:][c])
    formula(total1)
    for c in range(12):
        total2 += int(lista[c]) * int(lista1[c])
    total2 += formula(total1)
    formula(total2)
    return f'{formula(total1)}{formula(total2)}'


def formula(x):
    digito = 11 - (x % 11)
    if digito > 9:
        return 0
    else:
        return 1


def validando(x, y):
    if x == y:
        return 'Valido'
    else:
        return 'Invalido'


def gera():
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'
    cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}{terceiro_bloco}{quarto_bloco}'
    cnpj += total(cnpj)
    return cnpj
