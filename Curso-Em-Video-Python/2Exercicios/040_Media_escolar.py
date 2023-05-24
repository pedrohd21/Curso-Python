print('Escola Javali Cansado')
print('-' * 20)
nome = str(input('Qual seu nome: '))
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2)/2
if media < 5:
    print(' {} Sua media foi: {:.1f} \n REPROVADO!!'.format(nome, media))
elif media >= 5 and media < 7:
    print(' {} Sua media foi: {:.1f} \n RECUPERAÇÂO!!'.format(nome, media))
else:
    print(' {} Sua Media foi: {:.1f} \n APROVADO SEU LINDO!!'.format(nome, media))



