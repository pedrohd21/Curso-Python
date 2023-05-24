def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Error!! Digite um valor valido.')
        if ok:
            break
    return valor


#prograna principal
n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
