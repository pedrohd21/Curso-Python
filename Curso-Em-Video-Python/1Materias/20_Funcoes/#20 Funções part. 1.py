print('Apos fazer a def sempre pular 2 linhas')
'''
def linha(): # função sem parametro
    print('-' * 24)


linha()
print('      Hello Word')
linha()
'''

'''
def mensagem(msg): # função com parametro
    print('-' * 24)
    print(msg)
    print('-' * 24)


mensagem('Pedro')
mensagem('Hello mundo')
mensagem(f'{"oi":^24}')
'''

'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#programa principal
soma(b=4, a=6)
'''

'''
def contador(* num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números.')


contador(2, 1, 7) #forma uma tupla
contador(8, 1)
contador(4, 4, 7, 6, 2)
'''

'''
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''

def soma(* valores): # usando o * para add varios numeros
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)