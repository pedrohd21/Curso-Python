class Cliente:
    def __init__(self, nome, age, profession):
        self.nome = nome
        self.age = age
        self.profession = profession

    def adding_client(self):
        return [self.nome.upper(), self.age, self.profession.upper()]


class Dados:
    def pesquisar_clientes(self, cliente, lista):
        for c in lista:
            if c[0] == cliente:
                print(f'Encontrado: Nome: {c[0]}, Idade: {c[1]}, Profissão: {c[2]}')
                return
        print('Nada encontrado')

    def alterar_clientes(self, cliente, lista):
        for c in lista:
            if c[0] == cliente:
                c.clear()
                c.append(input('Nome: '))
                c.append(input('Idade: '))
                c.append(input('Profissão: '))

    def excluir(self, cliente, lista):
        for c in lista:
            if c[0] == cliente:
                c.clear()
                print('Excluido')