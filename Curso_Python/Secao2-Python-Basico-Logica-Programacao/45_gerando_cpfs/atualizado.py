cpf = '168.995.350-09'
cpf1 = cpf.replace('.', '')
cpf1 = cpf1.replace('-', '')

soma_primeiro = 0
soma_segundo = 0

soma1 = 10
soma2 = 11
for numero in range(0, 11, 1):
    if numero < 9:
        soma_primeiro += int(cpf1[numero]) * soma1
        soma1 -= 1

    if numero < 10:
        soma_segundo += int(cpf1[numero]) * soma2
        soma2 -= 1

digito1 = 11 - (soma_primeiro % 11)
digito2 = 11 - (soma_segundo % 11)

novo_cpf = str(cpf1[0:9])

if digito1 > 9:
    novo_cpf += str(0)

if digito2 == int(cpf1[10]):
    novo_cpf += str(digito2)

if cpf1 == novo_cpf:
    print('certo')
else:
    print('invalido')
