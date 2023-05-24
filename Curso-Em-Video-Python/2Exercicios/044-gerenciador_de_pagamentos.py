print('Nike')
print('-' * 30)
produto = float(input('Qual o valor do produto? R$ '))
pagamento = float(input('''[1] Pagamento a Vista com 10% de desconto Dinheiro ou Cheque
[2] A Vista no Cartão: 5% de Desconto
[3] Em até 2x no Cartão : Preço Normal
[4] 3x ou mais no cartão: 20% de Juros
Selecione a opção: 
'''))
if pagamento == 1:
    print('Valor atual do produto R$ {:.2f}, e o valor com 10% de desconto é R$ {:.2f}'.format(produto, (produto-(produto*10)/100)))
elif pagamento == 2:
    print('Valor atual do produto R$ {:.2f}, e o valor com 5% de desconto é R$ {:.2f}'.format(produto, (produto-(produto*5)/100)))
elif pagamento == 3:
    print('O valor do produto é R$ {:.2f}'.format(produto))
elif pagamento == 4:
    print('O valor sem Juros é R$ {:.2f}, e o valor com juros é: R$ {:.2f}'.format(produto, ((produto*20)/100)+produto))
else:
    print('Valor invalido')