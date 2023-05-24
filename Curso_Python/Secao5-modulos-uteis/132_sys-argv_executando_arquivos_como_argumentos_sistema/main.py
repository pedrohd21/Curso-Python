#  executa no terminal do pycharm

import sys
import os

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Faltando argumentos')
    print('-a', 'Para listar todos os arquivos nesta pasta ', sep='\t')
    print('-d', 'Para listar todos os diretorios nesta pasta', sep='\t')
    sys.exit()

so_file = False
if '-a' in argumentos:
    so_file = True

so_diretorios = False
if '-d' in argumentos:
    so_diretorios = True

for file in os.listdir('.'):
    if so_file:
        if os.path.isfile(file):
            print(file)

    if so_diretorios:
        if os.path.isdir(file):
            print(file)
