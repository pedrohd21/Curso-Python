import sys
import time

"""
def gera():
    r = []
    for n in range(100):
        yield n
        time.sleep(0.1)

    return r


g = gera()
"""
#   print(hasattr(g, '__iter__'))
#   print(hasattr(g, '__next__'))
#  print(next(g))  usar o next como for, mas executar so se escrever o comando um por um

"""
def gera():
    variavel = 'valor1'
    yield variavel
    variavel = 'valor2'
    yield variavel
    variavel = 'valor3'
    yield variavel


g = gera()
print(next(g))
print(next(g))
print(next(g))
"""

lista1 = [x for x in range(100000)]
lista2 = (x for x in range(100000))
print(sys.getsizeof(lista1))
print(sys.getsizeof(lista2))
