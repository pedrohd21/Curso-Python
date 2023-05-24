numero = int(input('Digite um numero: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
minhar = numero // 1000 % 10
print(' Unidade: {}\n Dezena : {}\n Centena: {}\n Milhar : {}'.format(unidade, dezena, centena, minhar))