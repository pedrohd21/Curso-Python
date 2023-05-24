'''n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, e a divisão {:.3f}, a divisão inteira é {}, e a potencia é {}'.format(s, m, d, di, e))
maior valor : max(numeros)
menor valor : min(numeros) ahahahahahhahahah'''

maior = menor = 0
for c in range(0, 4):
    valor = int(input('Digite um numero:'))
    if valor == 0:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
print(menor, maior)
