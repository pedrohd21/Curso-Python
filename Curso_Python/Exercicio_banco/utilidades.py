def func_parar():
    while True:
        parar = input('Deseja continuar? [S/N]').upper()
        if parar == 'S' or parar == 'N':
            break
        else:
            print('Digite S ou N.')
    if parar == 'N':
        return 'N'
