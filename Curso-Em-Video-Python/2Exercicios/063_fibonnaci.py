''' guanabara
print('Sequencia de Fibonacci')
n = int(input('Quantos termos você que mostrar? '))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')
cont =3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → Fim')'''
print('Feito por mim!!')
fibo = int(input('Quantos termos fibonacci? '))
t1 = 0
t2 = 1
t3 = 0
c = 3
print(' {} → {} → '.format(t1, t2), end='')
while c <= fibo:
    t3 = t1 + t2
    print('{} →'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(' Fim')
