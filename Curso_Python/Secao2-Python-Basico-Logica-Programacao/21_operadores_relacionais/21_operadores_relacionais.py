"""
Operadores Relacionais - aula 20
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente
"""
nome = str(input('Qual o seu nome: '))
idade = int(input('Idade: '))
if idade >= 18 and idade <= 32:
    print(f'{nome} tem idade pra pegar emprestimo.')
else:
    print(f'{nome} passou da idade de pegar emprestimo.')
