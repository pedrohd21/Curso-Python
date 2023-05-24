def porcento(n1, n2):
    return f'R$ {(n1 * n2 / 100) + n1:.2f}'


#numero1 = int(input('Quantos investir? '))
#numero2 = int(input('Quantos por cento de aumento? '))
print(porcento(50, 100))
