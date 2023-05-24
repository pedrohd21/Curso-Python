"""
Horario
Pedro Henrique
"""
hora = input('Digite um horario (0-23): ')
if 0 < int(hora) < 24:
    print(hora)
    try:
        if int(hora) < 12:
            print(f'{hora} Bom dia!!')
        elif int(hora) < 18:
            print(f'{hora} Boa tarde!!')
        elif int(hora) < 24:
            print(f'{hora}Boa noite!!')
        else:
            print('Error!! Digite uma hora valida de 0 a 24 horas')
    except:
        print('Error!! Digite um numero entre 0 e 24 inteiro.')
else:
    print('Invalido!! Numero entre 0 e 24')

""" Jeito prof
if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('Horário deve estar entre 0 e 23')
    else:
        if hora <= 11:
            print('Bom dia!')
        elif hora <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Por favor, digite um hórario entre 0 e 23.')
"""