# ex2: funcionario nome, salarioBruto, taxa, 
# 	salario, aumento
# 	APP salario liquido, porcentagem aumento, salario atualizado

class Funcionario:
    def __init__(self, nome, salario, taxa):
        self.nome = nome
        self.salario = salario
        self.taxa = taxa
    
    
    def aumento(self):
        self.salario += self.salario * self.taxa / 100
        return f'{self.nome} Salario atualizado: R${self.salario:.2f}'