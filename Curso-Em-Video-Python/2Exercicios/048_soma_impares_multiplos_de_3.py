cont = 0
soma = 0
for c in range(1, 501, 2):
    verificar = c % 3
    if verificar == 0:
        cont += 1
        soma += c
print('O total de numeros impares é {} e a soma entre eles é {}'.format(cont, soma))