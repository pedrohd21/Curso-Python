# Inicio
#
# def master(funcao):
#     def slave(*args, **kwargs):
#         print('Agora estou decorada.')
#         funcao(*args, **kwargs)
#     return slave
#
#
# @master
# def fala_oi():
#     print('Oi')
#
#
# @master
# def outra_funcao(msg):
#     print(msg)
#
#
# outra_funcao('Olá eu sou o Pedro')


# Inicio

from time import time
from time import sleep


def velocidade(funcao):
    """ Função decoradora: Verifica o tempo que uma função leva para executar """
    def interna(*args, **kwargs):
        """ Função que envolve e executa outra função """
        # Tempo inicial
        star_time = time()
        resultado = funcao(*args, **kwargs)
        # Executa a função
        end_time = time()
        # Tempo final
        tempo = (end_time - star_time) * 1000
        # Resultado de tempo em ms
        print(f'A função {funcao.__name__} levou {tempo:.2f}ms para executar')
    return interna
    # Retorna a função que envolve


@velocidade
def demora():
    for i in range(10000):
        print(i)


demora()
