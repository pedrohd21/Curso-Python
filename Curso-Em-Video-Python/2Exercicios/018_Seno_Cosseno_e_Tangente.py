from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno do angulo de {} é: {:.2f}'.format(angulo, seno))
print('O cosseno do angulo de {} é: {:.2f}'.format(angulo, cosseno))
print('A tangente do angulo {} é: {:.2f}'.format(angulo, tangente))
