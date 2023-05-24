progressao = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = progressao + (10 - 1) * razao
n = 0
ate = 9
total = 0
print('{}'.format(progressao), end="")
'''for c in range(progressao, decimo + razao, razao):
    print('{}'.format(c), end=' → ')'''
while n != ate:
    total += ate
    while n <= novo:
        n += 1
        progressao += razao
        print('-> {}'.format(progressao), end=" ")
    ate = int(input('Mais quantos termos: '))

