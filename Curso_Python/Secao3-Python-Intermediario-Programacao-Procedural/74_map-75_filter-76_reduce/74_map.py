from dados import produtos, pessoas, lista

# Multiplica a lista por 2
# nova_lista = map(lambda x: x * 2, lista)
# # print(list(nova_lista))
# nova_lista = [l * 2 for l in lista]  #list comprehension
# print(nova_lista)


# print('Outro Codigo a baixo')
# aumenta o preço em 5%
# def aumenta_preco(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p
#
#
# novos_produtos = map(aumenta_preco, produtos)
#
# for produto in novos_produtos:
#     print(produto)


print('Outro Codigo a baixo')


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20, 2)
    return p

nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)

