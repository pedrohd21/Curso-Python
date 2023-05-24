from random import randint
jogo = n = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 15)
while True:
    valor = int(input('Digite seu numero:'))
    jogada = str(input('Par ou Impar? ')).upper().split()[0]
    print('=-' * 15)
    pc = randint(0, 30)
    soma = (valor + pc) % 2
    if soma == 1:
        print(f'Você jogou {valor} e o computador {pc}. Total de {valor + pc} deu Impar')
    else:
        print(f'Você jogou {valor} e o computador {pc}. Total de {valor + pc} deu Par')
    if jogada == 'I' and soma == 1:
        print('Você venceu!!\nVamos Jogar novamente...')
    elif jogada == 'P' and soma == 0:
        print('Você venceu!!\nVamos Jogar novamente...')
    else:
        print('Você perdeu!!')
        n = 1
    if n == 1:
        break
    jogo += 1
print(f'Gamer Over! Você venceu {jogo}')
