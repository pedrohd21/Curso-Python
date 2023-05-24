lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Valor {c}°: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('=-' * 30)
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado é: {maior} nas posições ', end='')
for c, v in enumerate(lista):
    if v == maior:
        print(f'{c}...', end='')
print('')
print(f'O menor valor digitado é: {menor} nas posição ', end='')
for c, v in enumerate(lista):
    if v == menor:
        print(f'{c}...', end='')
