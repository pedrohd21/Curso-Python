from dados import produtos, pessoas, lista


# new_list = filter(lambda x: x > 5, lista) # feito com filter
# new_list = [x for x in lista if x > 5] # feito com list comprehension
# print(list(new_list))


# outro codigo
# def new_filter(produto):
#     if produto['preco'] > 50:
#         produto['e_caro'] = True
#     return True
#
#
# new_list = filter(new_filter, produtos)
#
# for c in new_list:
#     print(c)

# Outro codigo
def new_filter(pessoas):
    if pessoas['idade'] >= 18:
        pessoas['Maior_de_idade'] = pessoas['idade']
    else:
        pessoas['Menor_de_idade'] = pessoas['idade']
    return True


new_list = filter(new_filter, pessoas)

for produto in new_list:
    print(produto)
