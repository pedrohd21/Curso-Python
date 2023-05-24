numero = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    usu = int(input('Digite um numero entre 0 e 20: '))
    resp = len(numero)
    if 0 <= usu <= 20:
        break
    print('Tente novamente...')
print(f'O valor que voçê digitou é: {numero[usu]}')