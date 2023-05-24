from random import randint
soma = 0
resultado = 1
sorteio = randint(0, 10)
while resultado != 0:
    print('---' * 13)
    print('Vou escolher um numero entre 0 e 10 aleatoriamente')
    usuario = int(input('tente a sorte escolha um numero 1 a 10: '))
    soma += 1
    if sorteio == usuario:
        resultado = 0
        print('Parabéns você Venceu')
    elif sorteio < usuario:
        print('Menos... Tente mais uma vez.')
    else:
        print('Mais... Tente mais uma vez.')
print('Você precisou de {} tentativas'.format(soma))
