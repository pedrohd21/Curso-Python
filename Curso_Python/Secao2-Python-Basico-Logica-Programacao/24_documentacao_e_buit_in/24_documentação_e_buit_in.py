num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')
try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
    print('Error')