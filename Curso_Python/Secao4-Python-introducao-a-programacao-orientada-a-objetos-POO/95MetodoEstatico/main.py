from random import randint

class Pessoa: # metodo estatico, serve pra quando uma coisa serve pra todos
    staticmethod
    total = 2
    
    staticmethod
    def gera_id():
        rand = randint(1000, 199999)
        return f'Numero aleatorio: {rand}'
    

# print(Pessoa.gera_id())

print(Pessoa.total)
