n1 = (int(input('Digite um numero: ')),
      int(input('Digite outro numero: : ')),
      int(input('Digite mais um numero: : ')),
      int(input('Digite o ultimo numero: ')))
print(f'Os numeros digitados foram: {n1}')
par = 0
print(f'O numero 9 apareceu {n1.count(9)} vez')
if 3 in n1:
    print(f'O valor 3 apareceu na posição {n1.index(3)+ 1}°')
else:
    print('O valor 3 nn foi digitado')
for n in n1:
    if n % 2 == 0:
        par += 1
print(f'Os valores pares digitados foram {par}')
