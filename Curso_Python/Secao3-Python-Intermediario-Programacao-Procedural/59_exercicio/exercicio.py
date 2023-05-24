lista_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9,6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 1, 9, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
]


def encontra_duplicado(parametro):
    numeros_checados = set()
    primeiro_duplicado = -1
    for numero in parametro:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero)
    return primeiro_duplicado


for c in lista_inteiros:
    print(c, encontra_duplicado(c))


