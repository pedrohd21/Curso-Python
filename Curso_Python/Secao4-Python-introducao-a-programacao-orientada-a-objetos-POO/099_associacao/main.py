from classes import Escritor, Caneta, MaquinaDeEscrever


escritor = Escritor('Joanzinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

# print(escritor.nome)
# print(caneta.marca)
# maquina.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()


escritor.ferramenta = maquina
escritor.ferramenta.escrever()


