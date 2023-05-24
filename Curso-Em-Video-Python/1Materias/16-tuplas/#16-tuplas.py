'''Tuplas são imutaveis, nn da pra mudar'''
'''Da pra usar -1, -2, -3'''
'''lanche([1:3]) suco e pizza'''
'''lanche([2:]) vai da pizza ate o final'''
'''lanche([:2]) vai mostrar hamburge e suco ignora o ultimo'''

lanche = ('Hamburgue', 'Suco', 'Pizza', 'Pudim', 'Abobora')
print(lanche)
'''for c in lanche:
    print(F'Eu vou comer {c}')'''

''' --- Vai mostrar os numeros---
print(len(lanche))
print('Comi pra carai')'''

'''  --- Da pra usar dos dois jeitos dependendo do momento de uso---
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for comida in lanche:
    print(f'Eu vou comer{comida}')'''

''' --- Motra a posição e oq tem dentro---
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer{comida} na posição {pos}')'''

''' ---- deixa em ordem a variavel sorted ----
print(sorted(lanche))
'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
'''print(a)
print(sorted(a))
print(c)
print(sorted(c))
print('O len mostra o tamanho da tupla', len(c))
print('O count mostra quantos 5 tem na variavel, pode ser outros numeros pah pah pah', c.count(5))
print(c)
print('mostra onde ta na posição o numero, sempre mostra o primeiro a aparecer', c.index(4))
print('mostra onde ta na posição o numero, msm se existir outro igual', c.index(5, 1))
index tbm é usado para pesquisar as palavras'''

pessoa = ('Pedro', 23, 'M', 65.00)
del(pessoa)
'''Usar o del nn pode apagar um item especifico'''
print(pessoa)


''' Jeito mais facil bebe
d = {'A':10, 'B':5, 'C':55, 'D':99, 'E':59, 'F':20, 'G':44, 'H':79, 'I':1}
for c, e in list(d.items()):
    print(c, e)
'''
