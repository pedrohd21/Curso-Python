from random import randint
while True:
    cpf = str(randint(10000000000, 999999999999))

    atual_cpf = []

    inverte_cpf = atual_cpf[::-1]
    soma_cpf = 0
    for c in range(10, 1, -1):
        soma_cpf += c * int(inverte_cpf[c])

    #todo: Primeiro numero cpf
    calculo1 = 11 - (soma_cpf % 11)
    if calculo1 > 9:
        novo_cpf = atual_cpf[:9]
        novo_cpf.extend('0')
    else:
        novo_cpf = atual_cpf[:9]
        novo_cpf.extend('9')

    #todo: segundo Calculo do cpf
    inverte_cpf1 = novo_cpf[::-1]
    soma_cpf1 = 0
    for c in range(9, 0, -1):
        soma_cpf1 += c * int(inverte_cpf1[c])

    #todo: Segundo numero cpf
    calculo2 = 11 - (soma_cpf1 % 11)
    if calculo2 > 9:
        novo_cpf = atual_cpf[:10]
        novo_cpf.extend('0')
    else:
        novo_cpf = atual_cpf[:10]
        novo_cpf.extend('9')

    #todo: compara os cpf para ver se é válido
    if atual_cpf == novo_cpf:
        cpf_valido = ''
        for c in novo_cpf:
            cpf_valido += c
        print(f"Cpf válido: {cpf_valido}")
        break
    else:
        print('Analisando')