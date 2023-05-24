soma = 0
numero = int(input('Digite um numero: '))
for c in range(1, numero+1):
    if numero % c == 0:
        soma = soma + 1
print('O numero {} é divisivel por {} vezes'.format(numero, soma))
if soma == 2:
    print('E por isso ele É Primo')
else:
    print('E por isso Não É Primo!!')