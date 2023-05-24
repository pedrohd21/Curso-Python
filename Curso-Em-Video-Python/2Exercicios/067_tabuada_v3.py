tabu = n = 0
while True:
    n = 0
    tabu = int(input('Que ver a tabuada de qual valor? '))
    if tabu <= -1:
        break
    while n < 10:
        n += 1
        print(f'{tabu:2} X {n:2} = {tabu * n}')
print('Obrigado Volte Sempre!!')
