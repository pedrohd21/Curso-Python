dias = int(input('Quantos dias deseja alugar? '))
km = float(input('Quantos km foram rodados? '))
total = (dias * 60) + (km * 0.15)
print('O total a pagar é {:.2f}'.format(total))