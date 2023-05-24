# melhora a performace do codigo

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]  # multiplica cado elemento da lista 1 por 2

ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)

l2 = ['pedro', 'mauro', 'maria']
ex4 = [v.replace('a', '@').upper() for v in l2]  # muda a letra a de uma variavel
print(ex4)

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)  # inverter num dicionario
print(ex5['valor1'])

l3 = list(range(100))  # lista de 0 a 100
ex6 = [va for va in l3 if va % 3 == 0 if va % 8 == 0]  # numeros divisiveis por 3 e por 8
print(ex6)


ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex7)