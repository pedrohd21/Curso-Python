soma = 0
maior = 0
mulher = 0
for c in range(1, 5):
    print('-' * 5, '{}° Pessoa'.format(c), '-' * 5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    soma += idade
    if idade < 20 and sexo == 'F':
        mulher += 1
    if idade > maior and sexo == 'M':
        maior = idade
        nome1 = nome
print('A media de idade do grupo é {} anos'.format(soma/4))
print('O homem mais velho tem {} e se chama {}'.format(maior, nome1))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))