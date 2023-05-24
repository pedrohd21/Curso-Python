velocidade = int(input('Qual a velocidade do carro no radar? '))
if velocidade > 80:
    print('A cada km a cima da velocidade limite, a multa vai custar R$ 7,00 por cada km acimda da velocidade.')
    print('Valor da multa é: R${}'.format((velocidade - 80)*7))
print('dentro da velocidade permitida que é 80km.')