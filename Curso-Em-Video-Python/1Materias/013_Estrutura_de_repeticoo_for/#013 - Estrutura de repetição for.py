'''for c in range(6, 0, -1):
              (6, 0, -1) O -1 vai contar ao contrario e tbm da pra pular Ex(0, 6, 2)
    print(c)
print('Fim')'''

'''n = int(input('Digite um numero: '))
for c in range(n+1): # colocar o +1 para chegar no numero correto do usuario
    print(c)
print('Fim')'''

'''inicio = int(input('Qual numero começar a contagem? '))
fim = int(input('Contar ate que numero: '))
pular = int(input('Ir pulando em? '))
for contador in range(inicio, fim+1, pular):
    print(contador)
print('Fim')'''

s = 0
for contador in range(0,4):
    numero = int(input('Digite um numero: '))
    s += numero # += é a msm coisa que s+n=
print(s)