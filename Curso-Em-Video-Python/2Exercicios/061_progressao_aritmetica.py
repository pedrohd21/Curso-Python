progressao = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = progressao + (10 - 1) * razao
n = 0
ate = 9
print('{}'.format(progressao), end="")
'''for c in range(progressao, decimo + razao, razao):
    print('{}'.format(c), end=' → ')'''
while n != ate:
    n += 1
    progressao += razao
    print('-> {}'.format(progressao), end=" ")
cont = str(input('Deseja continuar? [S/N] ')).upper()
if cont == 'S':
    novo = int(input('Mais quantos termos: '))
    ate = novo + 1
else:
    print('Fim')