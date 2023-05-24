import random
n1 = str(input('Aluno: '))
n2 = str(input('Aluno: '))
n3 = str(input('Aluno: '))
n4 = str(input('Aluno: '))
lista = [n1, n2, n3, n4]
sorteio = random.shuffle(lista)
print('A ordem de apresentação é ')
print(lista)