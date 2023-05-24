frase = (str(input('Digite a frase: '))).split()
junto = ''.join(frase)
contrario = junto[::-1]
print('{} {}'.format(junto, contrario))
if junto == contrario:
    print('É Palindromo ')
else:
    print('Nn é Palindromo')