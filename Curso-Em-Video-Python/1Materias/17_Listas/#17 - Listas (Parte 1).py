'''print('Add numero')
num = [2, 5, 9, 1]
num[1] = 3
num.append(8)
num.sort() #ordem crescente
print(num)
num.sort(reverse=True) #ordem decrescente
print(num)
num.insert(2, 0) # troca o numero
print('Essa lista tem', len(num))

print('\n')

print('removendo numero')
num = [2, 5, 9, 1]
num.pop() # remove o ultimo intem
print(num)
num.pop(2) # remove o item desejado
print(num)
#num.remove(2) # ele vai eliminar o primeiro 2 que aparecer
if 4 in num: # procura o numero desejado
    num.remove(4)
else:
    print('Não encontei o numero 4')
print(num)'''
''' print('encontrar o valor desejado')
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c+1}° encontrei o valor {v}.')
'''

''' print('usuario add os numero!')
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c + 1} encontrei o numero {v}')
print('Cheguei ao final da lista.')
'''
'''
print('As listas viram uma so')
as listas se juntam, se mudar uma muda a outra
a = [2, 3, 4, 7]
b = a ####
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''

'''print('Lista nn ficam ligadas')
a = [2, 3, 4, 7]
b = a[:] # seleciona a lista toda
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''


