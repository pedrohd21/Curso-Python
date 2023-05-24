"""
Funções (def) em python - *args **kwargs
"""

"""
def func(a1, a2, a3, a4, a5, nome=None, a6=None):  # todo: depois de colocar o nome=None precisa nomear todas variáveis
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6


var = func(1, 2, 3, 4, 5, nome='Pedro', a6='5')
print(var[0], var[1])
"""


def func(*args, **kwargs):  # todo: criar uma tupla
    print(args)

    idade = kwargs['idade']
    print(idade)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Pedro', sobrenome='Henrique', idade=23)  # todo: desempacota a lista, e junta as duas lista ne uma só
