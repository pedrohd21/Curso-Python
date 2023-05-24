lista = list()
dados = []
maior = 0
menor = 9999
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    cont = str(input('Deseja continuar? [S/N] ')).upper()
    if cont == 'N':
        break
    elif cont == 'S':
        print('Add...')
    else:
        print('Opção invalida!!')

print(f'Ao todo foram Add {len(lista)} pessoas.')
print(f'O maior peso foi de {maior}. Peso de {pesado}')
print(f'O menor peso foi de {menor}. Peso de {leve}')
