from random import randint
soma = 0
resultado = 1
while resultado != 0:
    print('---' * 13)
    print('Vou escolher um numero entre 0 e 5 aleatoriamente')
    sorteio = randint(1, 5)
    usuario = int(input('tente a sorte escolha um numero 1 a 5: '))
    print('Processando...')
    soma += 1
    if sorteio == usuario:
        resultado = 0
        print('Parabéns você Venceu')
print('Você precisou de {} tentativas'.format(soma - 1))
print('---'*20)