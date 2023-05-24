cpf = '16899535009'

add_uma_string = 0
while add_uma_string <= 1:
    soma_cpf = 0
    reverso = 10 + add_uma_string
    for i in range(0, 9 + add_uma_string):
        soma_cpf += (reverso * int(cpf[i]))
        reverso -= 1

    #todo: Primeiro numero cpf
    calculo = 11 - (soma_cpf % 11)
    if calculo > 9:
        novo_cpf = cpf[:9 + add_uma_string]
        novo_cpf += '0'
    else:
        novo_cpf = cpf[:9 + add_uma_string]
        novo_cpf += '9'
    add_uma_string += 1

#todo: compara os cpf para ver se é válido
if cpf == novo_cpf:
    print(f'Cpf Válido')
else:
    print(f'Cpf Inválido')

