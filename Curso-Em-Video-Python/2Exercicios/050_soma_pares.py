soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        cont += 1
        soma += numero
print('O total de numeros pares é {} a soma é: {}'.format(cont, soma))