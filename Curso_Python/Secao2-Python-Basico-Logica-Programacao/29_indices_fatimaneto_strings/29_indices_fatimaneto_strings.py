"""
Manipulando strings - aula 30
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções buit-in len, abs, type, print, etc...
essas funçoes pode ser usadas diretamente em cada tipo.
"""
# positivos    [12345678]
texto       = 'Python s2'
# negativos   -[98765432]
print(texto[5]) #acessa apenas esse index
print(texto[:6]) #Começa do inicio ate a string desejada
print(texto[7:]) # Pega da 7 ate a ultima string
print(texto[0:6:2]) #0 é o inicio:6 é ate onde ir na variavel: 2 os pulos da variavekl
