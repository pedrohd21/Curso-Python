from datetime import date
atual = date.today().year
soma = 0
menor = 0
for c in range(1, 8):
    nascimento = int(input('Digite o ano do seu Nascimento: '))
    idade = atual - nascimento
    if idade >= 21:
        soma += 1
    else:
        menor += 1
print('Ao total {} são maiores de idade.'.format(soma))
print('Ao total {} são menores de idade.'.format(menor))
