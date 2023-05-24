

def lista_de_clientes(cliente_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(cliente_iteravel)
    return lista


clientes1 = lista_de_clientes(['João', 'maria', 'eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['Jose'])
print(clientes1)
print(clientes2)
print(clientes3)

