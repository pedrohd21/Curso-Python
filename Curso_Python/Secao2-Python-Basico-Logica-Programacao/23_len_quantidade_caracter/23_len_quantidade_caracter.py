""" Ex 1
usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)
if qtd_caracteres < 6:
    print('Digite pelo menos 6 caracteres.')
else:
    print('Você digitou a quantidade suficente de caracteres.')
"""
string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')
print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')
