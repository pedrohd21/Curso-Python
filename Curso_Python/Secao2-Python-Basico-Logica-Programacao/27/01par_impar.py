"""
Par ou impar
Pedro Henrique
"""
numero = input('Digite um numero inteiro: ')
try:
    if int(numero) % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é impar.')
except:
    print('Error!! Digite um numero inteiro.')
""" Prof
if not numero.isdigit():
    print('Isso não é um número inteiro.')
else:
    numero = int(numero)
    if not numero % 2 == 0:
        print(f'{numero} é impar.')
    else:
        print(f'{numero} é par.')
"""

""" Prof modo 2
if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')
else:
    print('Isso não é um numero inteiro.')
    """