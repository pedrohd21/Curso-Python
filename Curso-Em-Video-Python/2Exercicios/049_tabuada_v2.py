print('Tabuada')
print('-' * 20)
tabu = int(input('Qual Tabuada deseja Multiplicar: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(tabu, c, tabu*c))
print('Fim')