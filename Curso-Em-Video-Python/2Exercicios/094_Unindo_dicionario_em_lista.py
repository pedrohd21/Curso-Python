
dados = dict()
dados1 = list()
somaidade = 0
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [F/M] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Error!! Digite novamente.')
    dados['idade'] = int(input('Idade: '))
    dados1.append(dados.copy())
    while True:
        cont = str(input('Deseja continuar [S/N] ')).upper()[0]
        if cont in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    somaidade += dados['idade']
    if cont == 'N':
        break
media = somaidade / len(dados1)
print('=-' * 26)
print(f'A) Foi cadastrado {len(dados1)} pessoas')
print(f'B) A media de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for c in dados1:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print()
print('D) As idades acima da media foram: ')
for c in dados1:
    if c['idade'] > media:
        print(f'   nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]}')
print(f'{"<<Encerrado>>":^30}')

'''
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Error! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Error! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A media de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')'''