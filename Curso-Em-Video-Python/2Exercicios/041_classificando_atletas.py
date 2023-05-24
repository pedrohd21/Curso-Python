print('Confederação Nacional de Natação')
print('-' * 30)
idade = int(input('Qual a sua idade: '))
if idade < 10:
    print('Categoria Mirim')
elif idade < 15:
    print('Categoria Infantil')
elif idade < 20:
    print('Categoria Junior')
elif idade == 20:
    print('Categoria Senior')
else:
    print('Categoria Master')