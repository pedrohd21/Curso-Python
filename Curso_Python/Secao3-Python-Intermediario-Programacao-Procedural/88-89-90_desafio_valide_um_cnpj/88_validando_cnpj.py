from validando_cnpj import remover_caracteres, formula, validando, total, gera

cnpj = '04.252.011/0001-10'

numero_liso = remover_caracteres(cnpj)

lista_nova = numero_liso[0:12]

numeros_novos = (total(numero_liso))
lista_nova += numeros_novos

resultado_final = validando(numero_liso, lista_nova)
print(resultado_final)

for c in range(100):
    geras = gera()
    print(geras)

