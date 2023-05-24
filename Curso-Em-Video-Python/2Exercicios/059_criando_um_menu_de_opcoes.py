from time import sleep
menu = 0
numero1 = int(input('Numero 1: '))
numero2 = int(input('Numero 2: '))
while menu != 5:
    print('Menu')
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')
    menu = int(input('Selecione a opção: '))
    if menu == 1:
        print('A soma entre {} + {} = {}'.format(numero1, numero2, numero1+numero2))
    elif menu == 2:
        print('O produto entre {} x {} = {}'.format(numero1, numero2, numero1*numero2))
    elif menu == 3:
        if numero1 > numero2:
            print('O maior numero é: {}'.format(numero1))
        elif numero1 == numero2:
            print('Os numeros são iguais')
        else:
            print('O maior numero é: {}'.format(numero2))
    elif menu == 4:
        print('Novos numeros')
        numero1 = int(input('Digite um numero: '))
        numero2 = int(input('Digite um numero: '))
    elif menu == 5:
        print('Obrigado!!')
        print('Finalisando...')
        sleep(1)
    else:
        print('Opção invalida')
    print(':>' * 13)
