from time import sleep

'''
def cont(n1, n2, passo):
    print(f'Contagem de {n1} ate {n2} passo {passo} em {passo}')
    print('-' * 40)
    if n1 < n2 and passo >= 1:
        for c in range(n1, n2 + 1, passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
    elif n1 > n2 and passo >= 1:
        for c in range(n1, n2 - 1, -passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
    elif n1 > n2 and passo < 0:
        for c in range(n1, n2 - 1, passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
    elif n1 > n2 and passo == 0:
        for c in range(n1, n2 - 1, -1):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
        print('=-' *20)
    elif n1 < n2 and passo == 0:
        for c in range(n1, n2, 1):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
        print('=-' *20)


#Programa Principal
cont(1, 10, 1)
cont(10, 0, 2)
n1 = int(input('Inicio: '))
n2 = int(input('Fim: '))
passo = int(input('Passo: '))
cont(n1, n2, passo)
'''

def contador (i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=-'* 20)
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('FIm: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)