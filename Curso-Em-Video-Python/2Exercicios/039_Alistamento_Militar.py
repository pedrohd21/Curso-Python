from datetime import date
atual = date.today().year
print('ALISTAMENTO MILITAR BRASIL')
print('-' * 30)
nascimento = int(input('Qual ano voçê nasceu? '))
idade = atual - nascimento
if idade < 18:
    print('Você tem {} anos. Em {} voçe vai ta capacitado a se alistar.'.format(idade, nascimento+18))
elif idade == 18:
    print('Você tem {} anos. Ja pode se alistar, so se apresentar!!'.format(idade))
else:
    print('Você tem {} anos. Ja passou a hora de se alistar que era em {}'.format(idade, nascimento+18))