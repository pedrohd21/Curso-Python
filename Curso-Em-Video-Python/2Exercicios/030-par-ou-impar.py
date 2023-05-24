from math import trunc
numero = float(input('Digite um numero: '))
impar = numero % 2
if impar == 1:
    print('{} é impar'.format(trunc(numero)))
else:
    print('{} é par'.format(trunc(numero)))