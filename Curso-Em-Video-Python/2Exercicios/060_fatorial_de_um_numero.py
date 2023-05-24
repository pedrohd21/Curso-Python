fatorial = int(input('Digite um numero: '))
multiplicacao = 1
print('{}!= {}'.format(fatorial, fatorial), end="")
'''multiplicacao = 1
print('{}!= {}'.format(fatorial, fatorial), end="")
while fatorial != 1:
    multiplicacao = multiplicacao * fatorial
    fatorial = fatorial - 1
    print('x{}'.format(fatorial), end="")
print('= {}'.format(multiplicacao))'''
for c in range(fatorial - 1, 0, -1):
    print('x{}'.format(c), end="")
    multiplicacao *= c
print(' = {}'.format(multiplicacao * fatorial))