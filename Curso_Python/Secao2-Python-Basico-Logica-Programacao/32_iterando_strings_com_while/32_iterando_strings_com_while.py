"""
Iterando strings com while em python
"""
"""
minha_string = 'O rato roeu a roupa do rei de roma.'
tamanho_string = len(minha_string)
c = 0
nova_string = ''
while c < tamanho_string:
    if minha_string[c] == 'r':
        nova_string += minha_string[c].upper()
    else:
        nova_string += minha_string[c]
    c += 1
print(nova_string)
"""
minha_string = 'O rato roeu a roupa do rei de roma.'
tamanho_string = len(minha_string)
c = 0
contagem = 0
letra = ''
while c < tamanho_string:
    qtd_vezes_letra = minha_string.count(minha_string[c])
    if contagem < qtd_vezes_letra and minha_string[c].strip():
        letra = minha_string[c]
        contagem = qtd_vezes_letra
    #print(minha_string[c], conta)
    c += 1
print(letra, contagem)