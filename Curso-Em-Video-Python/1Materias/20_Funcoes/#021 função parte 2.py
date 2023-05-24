'''print('Ajuda Interativa')
print('Usando o help(e o comando)')
#help(print)'''

#exemplo DOCTRINGS**
'''def contador(i, f, p):
    """
    -> faz uma contagem e mostra na tela.
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')
resp = notas(10, 9, 8, sit=True)# Notas mostra a doctrings

help(contador)'''

#Exemplo parametros opcionais
'''def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: Segundo valor
    :param c: terceiro valor
    :return:
    """
    s = a + b + c
    print(f'A soma vale {s}')


soma(3, 2, 9)'''

#Escopo de Variavel
'''def teste(b):
    global a # faz o A valer oq ta dentro da função
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')'''

#Retornando Valores
'''def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)
print(f'Os resultados foram {r1}, {r2}, {r3}')'''


#Exercicio aula
print('Fatorial')
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')

print('Par e impar')
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')