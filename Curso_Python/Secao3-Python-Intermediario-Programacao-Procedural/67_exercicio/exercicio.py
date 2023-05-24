carrinho = []

carrinho.append(('produto 1', 30))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 3', 40))
carrinho.append(('produto 4', 50))

"""
total = 0
for produto in carrinho:
    total += produto[1]
print(total)
"""
"""
total = []
for produto in carrinho:
    total.append(produto[1])
print(total)
"""

total = sum([float(y) for x, y in carrinho])
print(total)

