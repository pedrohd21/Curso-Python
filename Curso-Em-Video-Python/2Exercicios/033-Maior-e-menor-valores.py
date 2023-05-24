n1 = int(input('Digite numero 1: '))
n2 = int(input('Digite numero 2: '))
n3 = int(input('Digite numero 3: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))