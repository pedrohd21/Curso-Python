"""
For in em python
iterando strings com for
Função rage(start=0, stop, step=1)
"""
"""
texto = 'Python'
for c in texto:
    print(c)
"""
"""
for n in range(20, 0, -1):
    print(n)
"""

texto = 'Python'
nova = ''
for c in texto:
    if c == 'y':
        nova += 'Y'
    else:
        nova += c
print(nova)


