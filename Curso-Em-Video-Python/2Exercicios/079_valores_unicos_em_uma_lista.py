lista = list()
while True:
    valor = int(input('Digite um Valor: '))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if valor not in lista:
        lista.append(valor)
        print('valor adicionado com sucesso...')
    else:
        contador
        print('Valor duplicado! não vou adicionar...')
    if continuar in 'N':
        break
    #if lista.count(valor) == 2:
        #print('Valor duplicado não vou adicionar...')
        #lista.pop()
    #elif continuar == 'N':
        #break
print(f'Lista foi {sorted(lista)}')
