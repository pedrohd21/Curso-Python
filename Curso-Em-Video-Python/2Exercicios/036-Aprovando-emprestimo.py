print('Simulador de Casa')
print('-' * 50)
ValorCasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salario? R$ '))
ano = int(input('Quantos anos prentende pagar a casa? '))
meses = ValorCasa / (ano * 12)
total = (salario * 30)/100
print('-' * 50)
if total > meses:
    print('Aprovado!!')
    print('Você vai pagar {:.2f} Por mês'.format(meses))
else:
    print('Negado!!')
    print('Você não foi aprovado.')
print('Obrigado por ter usado nossos serviços')