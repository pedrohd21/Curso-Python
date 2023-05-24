from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'C'},
    {'nome': 'Rosemary', 'nota': 'D'},
    {'nome': 'Joana', 'nota': 'A'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'Eduardo', 'nota': 'A'},
    {'nome': 'Andre', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'Jose', 'nota': 'B'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, lambda item: item['nota'])
for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)  # Cria uma copia

    print(f'agrupamento: {agrupamento}')
    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t {quantidade} alunos tiraram a nota {agrupamento}')
