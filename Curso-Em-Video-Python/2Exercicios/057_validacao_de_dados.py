sexo = 1
while sexo != 0:
    resposta = str(input('Qual o seu sexo: [M/F] ')).upper()[0]
    if resposta == 'M' or resposta == 'F':
        sexo = 0
        if resposta == 'M':
            print('Correto!! Sexo Masculino!!')
        if resposta == 'F':
            print('Correto!! Sexo Feminino!!')
    else:
        print('Opção invalida. Por favor, ', end="")
print('Obrigado!')
