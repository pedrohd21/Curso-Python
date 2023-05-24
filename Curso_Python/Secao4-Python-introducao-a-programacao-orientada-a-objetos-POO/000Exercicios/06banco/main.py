from banco import Banco


numero = input('Numero Conta: ')
nome = input('Nome: ')

deposito_inicial = input('Deseja fazer deposito inicial [S/N]? ').upper()

print(deposito_inicial)
if deposito_inicial[0] == 'S':
    saldo = float(input('Valor deposito inicial: R$ '))
    b1 = Banco(numero, nome, saldo)
    print('Valores atualizados:')
    print(f'Conta: {b1.numero}, Usuario: {b1.nome}, Saldo Atual: R${b1.saldo:.2f}')


