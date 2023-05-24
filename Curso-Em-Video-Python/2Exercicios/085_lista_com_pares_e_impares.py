from random import randint
dados = [[], []]
valor = 0
for c in range(0, 7):
    valor = randint(1, 10)
    #valor = int(input(f'Digite o {c + 1}° Valor: '))
    if valor % 2 == 0:
        dados[0].append(valor)
    else:
        dados[1].append(valor)
dados[0].sort()
dados[1].sort()
print(f'Os valores pares digitados foram: {dados[0]}')
print(f'Os valores impares digitados foram: {dados[1]}')

