n = soma = 0
valor = int(input('Valor: '))
while valor != 999:
    soma += valor
    n += 1
    valor = int(input('Valor: '))
print('O total de numeros digitados foi {}, e a soma entre eles foi {}'.format(n, soma))
