"""Introdução à formatação de Strings"""

nome = 'Pedro'
idade = 23
altura = 1.80
e_maior = idade > 18
peso = 60
imc = peso / (altura**2)
"""print('Nome: ', nome)
print('Idade: ', idade)
print('Idade: ', idade)
print('Maior de idade: ', altura)"""
print(nome, 'tem', idade, 'e seu imc é:', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{n} tem {i} anos de idade e seu imc é {imc:.2f}'.format(n=nome, i=idade, im=imc))
#todo: com o format em print da pra colocar a ordem que quiser a variavel.