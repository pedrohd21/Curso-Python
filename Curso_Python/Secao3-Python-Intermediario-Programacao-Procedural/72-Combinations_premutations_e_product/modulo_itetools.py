"""
Combinations, Permutations e Product - Itertools
combinação - Ordem não importa
permutação - ordem importa
ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product
pessoas = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']
# for grupo in combinations(pessoas, 2):  # Ordem não importa
#     print(grupo)

# for grupo in permutations(pessoas, 2):  # Ordem aleatoria
#     print(grupo)

for grupo in product(pessoas, repeat=2):  # Todas combinações possiveis
    print(grupo)

a = ['a', 'b', 'c']

for c in product(a, repeat=2):
    print(c)