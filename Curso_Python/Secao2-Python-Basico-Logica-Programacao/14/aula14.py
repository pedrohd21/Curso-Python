from datetime import date
nome = 'Pedro'
idade = 23
altura = 1.76
peso = 60
imc = peso / (altura ** 2)
ano = date.today().year - 24
print(f'{nome} tem {idade}, {altura} e pesa {peso}Kg.\nO IMC de {nome} é {imc:.2f}\n{nome} nasceu em {ano}.')
