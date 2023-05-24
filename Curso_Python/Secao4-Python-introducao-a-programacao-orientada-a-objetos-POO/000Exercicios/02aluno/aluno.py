# ex: aluno nome, nota, 
# 	media e total
# 	App 4 notas

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    
    def total(self, nota):
        self.nota += nota
    
    def resultado(self):
        resultado = self.nota / 4
        if resultado >= 6:
            return f'{self.nome}, Total: {resultado}, Media: {resultado}, Aprovado'
        if resultado >= 5:
            return f'{self.nome}, Total: {resultado}, Media: {resultado}, Recuperação'
        else:
            return f'{self.nome}, Total: {resultado}, Media: {resultado}, Reprovado'

            