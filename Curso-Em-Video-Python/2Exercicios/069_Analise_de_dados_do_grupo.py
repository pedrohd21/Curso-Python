n = sexo = 'M'
maioridade = mulheres = homens = 0
print('=-' * 20)
print('ANALISE DE DADOS')
print('=-' * 20)
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual o seu sexo: [M/F] ')).upper().split()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    n = str(input('Deseja Continuar? [S/N]')).upper().split()[0]
    if n == 'N':
        break
print(f' {maioridade} pessoas tem mais de 18 anos \n {homens} homens foram cadastrados \n {mulheres} mulheres e com menos de 20 anos')

print('Volte sempre!!')