"""
public, protected, private
"""

class BaseDeDados:
    self.dados = {}
    
    def inserir_cliente(self):
        if 'clientes' not in self.dados:
            self.dados['cliente'] = {id: nome}
        else:
            self.dados['cliente'].update({id: nome})
        
    

bd = BaseDeDados()
