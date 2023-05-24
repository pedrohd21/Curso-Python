from math import hypot
co = float(input('Quanto medo o cateto oposto: '))
ca = float(input('Quanto medo o cateto adjacente: '))
hipotenusa = hypot(co, ca)
'''hipotenusa = (ca**2 + co**2) ** (1/2) formula matematica
print('O a soma dos quadrado dos catetos de um triângulo retângulo é igual ao quadrado de sua hipotenusa: {:.2f}'.format(hipotenusa))'''
'''Formula Facil pelo math abaixo '''
print('A soma da hipotenusa é {:.2f}'.format(hipotenusa))

