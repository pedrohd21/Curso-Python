print('Conversor de bases numericas: ')
print('-' * 40)
print('Escolha das bases de conversão: ')
n = int(input('''[1] converter para binario 
[2] converter para octal 
[3] converter para Hexagonal 
Sua opção foi: '''))
n1 = int(input('Digite um numero: '))
if n == 1:
    print('A conversão para Binario é {}.'.format(bin(n1)[2:]))
elif n == 2:
    print('A conversão para Octal é {}.'.format(oct(n1)[2:]))
elif n == 3:
    print('A conversão para Hexagonal é {}.'.format(hex(n1)[2:]))
else:
    print('Opção invalida')

