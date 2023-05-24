turma = []
nota = []
nome = []
pessoas = 0
totmedia = []
cont = 0
while True:
    nome.append(str(input('Nome: ')))
    media = 0
    for c in range(1, 3):
        nota = float(input(f'Nota {c}: '))
        media = media + nota
        nome.append(nota)
    turma.append(nome[:])
    totmedia.append(media)
    nome.clear()
    cont = str(input('Deseja continuar: [S/N] ')).upper()
    pessoas += 1
    if cont == 'N':
        break

print('=-'*15)
print(f'{"N°":<4}{"Nome":<11}{"Média"}')
print('-'*30)

for p in range(0, pessoas):
    print(f'{p:<4}{turma[p][0]:<11}', end='')
    for c in range(0, 1):
        print(f'{totmedia[p] / 2:.2f}')

while True:
    cont = int(input('Mostra notas de qual aluno? (999 interrompe): '))
    if cont == 999:
        break
    for c in range(0, 1):
        print(f'Notas de {turma[cont][0]} são', end=' ')
        for i in range(1, 3):
            print(f'[{turma[cont][i]:.2f}]', end=' ')
        print()
