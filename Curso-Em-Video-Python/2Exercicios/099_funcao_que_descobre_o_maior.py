from time import sleep

def maior(* numero):
    print('=-' * 20)
    print('Analisando os valores passados...')
    maior_num = 0
    for c in numero:
        print(c, end=' ')
        sleep(0.5)
        if c > maior_num:
            maior_num = c
    print(f'Foram informados {len(numero)} valores ao todo.')
    print(f'O maior valor informado foi: {maior_num}')


#programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
