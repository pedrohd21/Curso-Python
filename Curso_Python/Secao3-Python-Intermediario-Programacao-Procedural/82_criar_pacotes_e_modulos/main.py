# import vendas.calcula_preco
from vendas import calcula_preco
from vendas.formata import preco as preco2


preco = 49.99
preco_com_aumento = calcula_preco.aumento(preco, 15, formata=True)
print(preco_com_aumento)

preco_com_reducao = calcula_preco.reducao(preco, 15, formata=True)
print(preco_com_reducao)

print(preco2.real(59.99))
