matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
impar = soma = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-' * 30)
for l in range(0, 3):
    print(f'[{matriz[0][l]:^3}]', end=' ')
print()
for l in range(0, 3):
    print(f'[{matriz[1][l]:^3}]', end=' ')
print()
for l in range(0, 3):
    print(f'[{matriz[2][l]:^3}]', end=' ')
print()
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
for l in range(0, 3):
    soma += matriz[l][2]
for c in range(0, 3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
print(par)
print(soma)
print(maior)