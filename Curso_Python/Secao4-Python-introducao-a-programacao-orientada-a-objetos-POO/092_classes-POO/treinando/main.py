from treinando import IndoShow

p1 = IndoShow()

# Ingresso acabou
p1.fila()
p1.fila()
p1.acabou()
p1.comprando_ingresso()
print('#' * 30)
# Tem o ingresso
p1.fila()
p1.fila()
p1.comprando_ingresso()
p1.transporte('719')
p1.durante_show('foda'.upper())

