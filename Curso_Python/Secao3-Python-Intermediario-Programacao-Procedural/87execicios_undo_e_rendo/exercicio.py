

def menus():
    while True:
        print("""Menu:
        1) Nova tarefa
        2) Apagar tarefa anterior
        3) Refazer tarefa apagadas
        4) Sair
        """)
        menu = int(input('Selecione uma opção: '))
        if menu == 1:
            nova_tarefa()
        elif menu == 2:
            apagar_tarefa()
        elif menu == 3:
            print(refazer_tarefa())
        elif menu == 4:
            break
        else:
            print('Digite uma opção valida.')
            break
        lista_ate_aq()


def lista_ate_aq():
    print('-' * 30)
    print('Lista de Tarefas')
    for k, v in enumerate(tarefas):
        print(f'Tarefa {k + 1}:', end='')
        print(f'    {v}')
    print('-' * 30)


def nova_tarefa():
    while True:
        tarefa = str(input('Digite a tarefa: '))
        tarefas.append(tarefa)
        tarefas_apagadas.append(tarefa)
        while True:
            para = str(input('Deseja parar? [S/N] ')).upper()[0]
            if para == 'S' or 'N':
                break
            else:
                print('Digite uma opção valida.')
        if para == 'S':
            break


def apagar_tarefa():
    tarefas.pop()


def refazer_tarefa():
    if len(tarefas_apagadas) > len(tarefas):
        tarefas.append(tarefas_apagadas[len(tarefas)])
    else:
        return 'Chegou no maximo'


if __name__ == '__main__':
    while True:
        tarefas = []
        tarefas_apagadas = []
        menus()
        lista_ate_aq()
