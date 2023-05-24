n = 'N'
para = 'S'
maior = 0
menor = 9999
media = 0
digitados = 0
while n != para:
    valor = int(input('Digite um numero: '))
    para = str(input('Deseja continuar: [S/N] ')).upper()
    media += valor
    digitados += 1
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
print('A media foi {}'.format(media / digitados))
print('Menor ', menor)
print('Maior ', maior)