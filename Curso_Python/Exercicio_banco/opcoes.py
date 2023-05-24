from utilidades import *
from dados.dados import Cliente, Dados

lista_clientes = list()


def func_opcoes(op=0):
    if op == 1:
        while True:
            nome = input('Nome: ').upper()
            idade = input('Idade: ')
            profissao = input('Profissão: ').upper()
            add = Cliente(nome, idade, profissao)
            lista_clientes.append(add.adding_client())
            parar = func_parar()
            if parar == 'N':
                break

    elif op == 2:
        for clientes in lista_clientes:
            print(clientes)

    elif op == 3:
        dados = Dados()
        nome = input('Cliente Pesquisar Nome: ').upper()
        dados.pesquisar_clientes(nome, lista_clientes)

    elif op == 4:
        dados = Dados()
        nome = input('Cliente Alterar Nome: ').upper()
        dados.alterar_clientes(nome, lista_clientes)
    elif op == 5:
        dados = Dados()
        nome = input('Cliente Excluir Nome: ').upper()
        dados.excluir(nome, lista_clientes)
