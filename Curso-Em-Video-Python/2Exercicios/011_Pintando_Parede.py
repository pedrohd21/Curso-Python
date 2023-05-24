larg = float(input('largura da parede: '))
alt= float(input('Altura da parede: '))
area = larg* alt
tinta = area/2
print('Sua parede tem a dimenção de {} x {} e sua área é de {}'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {} L de tinta'.format(tinta))