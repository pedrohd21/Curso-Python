def voto(ano):
    from datetime import date
    v = date.today().year - ano
    print(f'Com {v} anos: ', end='')
    if v >= 18:
        return 'VOTO OBRIGATORIO!!'
    elif v >= 65:
        return 'VOTO OPCIONAL!!'
    else:
        return 'NÃO VOTA!!'


#programa Principal
print(f'{"URNA ELEITORAL":^25}')
print('-' * 25)
nascimento = int(input('Em que ano voçê nasceu? '))
print(voto(nascimento))