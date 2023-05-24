c = 's'
valores = []
while c != 'N':
    valor = int(input('Digite um valor: '))
    c = str(input('Quer continuar? [S/N] ')).upper()
    valores.append(valor)
print(valores)
print(f'Voçê digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente é: {valores}')
if valores.count(5):
    print(f'O valor 5 foi encontrado na lista')
else:
    print(f'O valor 5 não foi encontrado na lista')
