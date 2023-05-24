nome = input('Qual o seu nome: ')
if len(nome) < 5:
    print(f'{nome} seu nome é Pequeno.')
elif len(nome) < 8:
    print(f'{nome} seu nome é Normal.')
else:
    print(f'{nome} seu nome é Muito Grande.')