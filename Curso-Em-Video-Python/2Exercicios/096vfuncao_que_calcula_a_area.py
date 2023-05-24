print(f'{"Controle de terreno":^30}')
def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.2f} x {c:.2f} é de {a}m².')


#Programa principal
largura = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(largura, comp)
