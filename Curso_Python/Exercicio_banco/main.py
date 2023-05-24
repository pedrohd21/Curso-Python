from opcoes import func_opcoes
from utilidades import *

lista_clientes = list()

if __name__ == '__main__':
    while True:
        opcoes = int(input('''
Selecione a opção: 
[1] Cadastras Pessoas
[2] Lista de Clientes
[3] Pesquisar Clientes
[4] Alterar Dados
[5] Excluir Clientes
[6] Sair
    Selecione: '''))
        func_opcoes(opcoes)
        print()
        if opcoes == 6:
            print('Saindo')
            break




