'''filme = {
    'Titulo':'Star Wars',
    'ano': 1997,
    'Diretor': 'George Lucas'
}
#print(filme.values()) #mostra o imput da variavel
#print(filme.keys()) # mostra a varial ex nome
for k, v in filme.items():
    print(f'O {k} é {v}')'''


'''
pessoas = {'nome':'Pedro', 'sexo': 'M', 'idade': 22}
del pessoas['sexo'] #apaga o sexo

pessoas['nome'] = 'Gustavo' # da pra mudar o dicionario
pessoas['peso'] = 98

#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

#print(pessoas.keys())

#print(pessoas.values())

#print(pessoas.items())

for k in pessoas.keys(): 
    print(k)
    
for k in pessoas.values():
    print(k)
    
for k, v in pessoas.items():
    print(k, v)
'''

'''
brasil = []
estado1 = {'uf' : 'Rio de janeiro', 'Sigla': 'Rj'}
estado2 = {'uf': 'São Paulo', 'Sigla': 'Sp'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['Sigla'])
'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for k in brasil:
    for v in k.keys():
        print(v, end=' ')
    print()