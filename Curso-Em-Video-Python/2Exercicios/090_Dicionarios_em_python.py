'''aluno = {}
aluno['nome'] = str(input('Qual o Seu nome: '))
aluno['media'] = float(input('Qual a sua media: '))
print(f'Nome igual a {aluno["nome"]}\nMedia igual a {aluno["media"]:.2f}')
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print(f'A situação do aluno {aluno["nome"]} é {aluno["situação"]}')'''

print('Resolvido pelo guanabara')
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
print(aluno)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')