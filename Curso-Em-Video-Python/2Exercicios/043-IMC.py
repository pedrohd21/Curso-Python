print('Indice de massa corporal')
print('-' * 20)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura ** 2)
if imc < 18.5:
    print('Seu imc é {:.2f}. ABAIXO DO PESO!!'.format(imc))
elif imc >=18.5 and imc <= 25:
    print('Seu imc é {:.2f}. PESO IDEAL!!'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu imc é {:.2f}. SOBREPESO!!'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu imc é {:.2f}. OBESIDADE!!'.format(imc))
else:
    print('Seu imc é {:.2f}. OBESIDADE MÓRBIDA!!'.format(imc))