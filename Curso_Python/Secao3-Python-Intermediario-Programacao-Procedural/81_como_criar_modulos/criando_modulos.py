import math
pi = math.pi


def dobra_lista(lista):
    return [x*2 for x in lista]


def multiplica(lista):
    r1 = 1
    for i in lista:
        r1 += i
    return r1


lista = [1, 2, 3, 4, 5]
if __name__ == '__main__': # Não vai ser executado no outro arquivo que importa esse
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(pi)

# print(__name__) mostra o nome do arquivo quando importa ele
