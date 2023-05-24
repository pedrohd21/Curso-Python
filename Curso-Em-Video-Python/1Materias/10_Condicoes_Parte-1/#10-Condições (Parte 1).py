nome = str(input('Digite seu nome: '))
if nome == 'Pedro':
    print('Que nome lindo!!')
else:
    print('Que nome fudido!!')

nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
media = (nota1 + nota2)/2
print('Sua media é {:.2}'.format(media))
if media < 6:
    print('Abaixo da media.')
else:
    print('Acima da media.')