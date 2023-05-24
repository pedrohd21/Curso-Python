"""
For / Else em python
"""
variavel = ['Luiz Otavio', 'Joãozinho', 'Maria']
for valor in variavel:
    print(valor)
    if valor.startswith('M'):
        print('Começa com J', valor)
    else:
        print('Não começa com J')