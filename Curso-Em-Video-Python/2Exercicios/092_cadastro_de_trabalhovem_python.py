'''
from datetime import date
atual = date.today().year
dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = atual - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] == 0:
    print('=-'*13)
    print(f'{"Dados da Pessoa":^26}')
    print('=-' * 13)
    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {dados["idade"]} anos')
    print(f'ctps: Não possui')
else:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Valor do Salario: R$ '))
    print('=-' * 13)
    print(f'{"Dados da Pessoa":^25}')
    print('=-' * 13)
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - date.today().year
    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {dados["idade"]} anos')
    print(f'ctps: {dados["ctps"]}')
    print(f'Foi contratado em {dados["contratação"]}')
    print(f'Salario é de R$ {dados["salario"]:.2f}')
    print(f'Você vai se aposentar com {dados["aposentadoria"]} anos')
'''

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano da contratação: '))
    dados['salario'] = float(input('Salario: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('=-' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')