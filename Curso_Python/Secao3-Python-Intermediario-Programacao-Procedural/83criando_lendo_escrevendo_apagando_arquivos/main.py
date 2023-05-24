# https://docs.python.org/3/library/functions.html#open

# Obs: 'w+' cria um arquivo do zero
# Obs: 'a+' vai add mais coisas ao arquivo
# Obs: 'r' vai ler o arquivo

# Começo do codigo
# file = open('abc.txt', 'w+')
# file.write('linha 1\n')
# file.write('linha 2\n')
# file.write('linha 3\n')
#
# file.seek(0, 0)  # Mostra tudo
# print('Lendo Linhas')
# print(file.read())
# print('#' * 20)
#
# file.seek(0, 0)
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
#
# file.seek(0, 0)
#
# print('#' * 20)
# for linha in file.readlines():
#     print(linha, end='')
# file.close()


# Começo do codigo
# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0, 0)
#     print(file.read())
# finally:
#     file.close()

# Comeco do codigo melhor jeito de fazer
# with open('abc.txt', 'w+') as file:
#     file.write('linha 1 ')
#     file.write('linha 2 ')
#     file.write('linha 3')
#     file.seek(0)
#     print(file.read())

# comeco do codigo
# with open('abc.txt', 'r') as file:  # 'r' Vai apenas ler o arquivo
#     print(file.read())

# Comeco do codigo
with open('abc.txt', 'a+') as file:  # 'a+' Vai adicionar sem apagar ele
    file.write(' Outra linha')
    file.seek(0)
    print(file.read())

