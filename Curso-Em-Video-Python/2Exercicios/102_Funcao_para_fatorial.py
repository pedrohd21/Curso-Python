def fatorial(n=1, show=False):
    """
    -> calcula o fatorial de um numero.
    :param n: O numero a ser calculado
    :param show: (Opcional) mostra ou não a conta.
    :return: retorna o fatorial de um numero
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa Principal
print(fatorial(5, show=True))
help(fatorial)
