# add(adiciona), update(atualiza), clear, discard
# Union | (une)
# interection & (todos os elementos presentes nos dois sets)
# differense - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)
# Não adicona elementos duplicados
"""
s1 = {1 ,2, 3, 4, 5}

for v in s1:
    print(v)
"""
"""
s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
print(s1)

s1.discard(2)
"""
"""
l1 = [1, 2, 1, 1, 3, 4, 5, 6, 6, 6, 6, 7, 8, 9, 'Pedro', 'Pedro']
l1 = set(l1)
print(l1)
"""
"""
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 | s2 # | une os sets, & une todos elementos que estão nas variaveis
print(s3)
"""
l1 = ['Pedro', 'Luiz', 'Maria']
l2 = ['Pedro', 'Luiz', 'Maria', 'Maria', 'Maria', 'Maria', ]
if set(l1) == set(l2):
    print('L1 é igual a l2')
else:
    print('l1 não é igual a l2')