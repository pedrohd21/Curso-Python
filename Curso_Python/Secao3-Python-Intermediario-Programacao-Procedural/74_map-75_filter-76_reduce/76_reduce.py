from dados import produtos, pessoas, lista
from functools import reduce
# Inicio Codigo -------------------------------
# sum_list = reduce(lambda acu, it: it + acu, lista, 0) # soma a lista
# print(sum_list)


# inicio codigo ---------------------
# sum_prices = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
# print(round(sum_prices / len(produtos), 2))

# inicio codigo-----------------------
sum_the_age = reduce(lambda accumulator, people: people['idade'] + accumulator, pessoas, 0)
print(round(sum_the_age / len(pessoas), 2))
