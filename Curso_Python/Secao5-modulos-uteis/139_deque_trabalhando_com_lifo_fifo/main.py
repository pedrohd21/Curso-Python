"""
Pilhas e filas
Pilhas (stack) - LIFO - last in, first out.
    Exemplo: Pilhas de livros que são adicionados um sobre o outro
Fila (queue) - FIFO - first in, first out.
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeito colaterais em desempenho, porque cada item
alterado, todos os indices serão modificados.
"""
"""
from _collections import deque

fila = deque()
fila.append('Joãozinho')
fila.append('Maria')
fila.append('Luiz Otávio')
fila.append('Marcos')
fila.append('José')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
for nome in fila:
    print(nome)
"""
"""
from collections import deque

fila = deque(maxlen=10)
for c in range(500):
    fila.append(c)
    print(fila)
"""
from collections import deque

fila = deque(maxlen=10)
fila.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
fila.insert(2, 'Pedro')
print(fila)
