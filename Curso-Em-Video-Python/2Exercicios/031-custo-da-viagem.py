distancia = int(input('Digite a distancia da sua viagem: '))
if distancia < 201:
    print('o valor da passagem é: R$ {:.2f}'.format(distancia * 0.50))
else:
    print('O valor da passagem é: R$ {:.2f}'.format(distancia * 0.45))