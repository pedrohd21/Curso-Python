#if:
#elif: pode usar quantos quiser
#else:
nome = str(input('Qual o seu nome: '))
if nome == 'Pedro':
    print('Que belo nome {}'.format(nome))
elif nome == 'Gustavo' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil'.format(nome))
else:
    print('Que nome sem graça {}'.format(nome))
print('Tenha um bom dia {}'.format(nome))


''' ---  da pra usar assim tbm ---
    if 0 <= n <= 20:
    ai fica entre um numero de 0 a 20
'''