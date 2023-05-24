a = lambda x, y: x * y
print(f'Função lambda {a(2,2)}')


lista = [
    ['P1', 13, 15],
    ['P2', 6, 20],
    ['P3', 7, 26],
    ['P4', 50, 90],
    ['P5', 8, 100]
]
lista.sort(key=lambda i: i[1])  # todo: Da pra colocar na ordem e inverter
print(lista)
print(sorted(lista, key=lambda i: i[0], reverse=True))  # todo: Ou inverter e colocar na ordem assim

