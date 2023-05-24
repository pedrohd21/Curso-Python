frase = str(input('Digite uma frase: ')).upper().strip()
print(' Quantos *A* possui:  {}\n Primeiro *A*: {}\n Segundo *A*: {}'.format((frase.count('A')), (frase.find('A')+1), (frase.rfind('A')+1)))
