"""
Sistema de perguntas e respostas
"""
print()
print('Desafio multipla escolha.')

print('=' * 28)
pergutas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'respostas_certas': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 * 2? ',
        'respostas': {'a': '6', 'b': '4', 'c': '5'},
        'respostas_certas': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 9 * 7? ',
        'respostas': {'a': '50', 'b': '63', 'c': '70'},
        'respostas_certas': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 50 / 2? ',
        'respostas': {'a': '26', 'b': '20', 'c': '25'},
        'respostas_certas': 'c',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 1000 / 100? ',
        'respostas': {'a': '200', 'b': '100', 'c': '10'},
        'respostas_certas': 'c',
    },
    'Pergunta 6': {
        'pergunta': 'Quanto é 120 + 280? ',
        'respostas': {'a': '400', 'b': '380', 'c': '800'},
        'respostas_certas': 'a',
    },
    'Pergunta 7': {
        'pergunta': 'Quanto é 100 * 10? ',
        'respostas': {'a': '200', 'b': '10000', 'c': '1000'},
        'respostas_certas': 'c',
    },
    'Pergunta 8': {
        'pergunta': 'Quanto é 1 * 1? ',
        'respostas': {'a': '2', 'b': '1', 'c': '0'},
        'respostas_certas': 'b',
    },
    'Pergunta 9': {
        'pergunta': 'Quanto é 0 * 10? ',
        'respostas': {'a': '10', 'b': '0', 'c': '5'},
        'respostas_certas': 'b',
    },
    'Pergunta 10': {
        'pergunta': 'Quanto é 500 + 501? ',
        'respostas': {'a': '1002', 'b': '1000', 'c': '1001'},
        'respostas_certas': 'c',
    },
}
respostas_certas = 0
for pk, pv in pergutas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ').lower()
    if resposta_usuario == pv['respostas_certas']:
        print('EHHH!!! Você acertou!!!!')
        respostas_certas += 1
    else:
        print('IXIIII!! Você ERROU!!!!')
    print()

porcentagem_acerto = respostas_certas / len(pergutas) * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto:.2f}%.')