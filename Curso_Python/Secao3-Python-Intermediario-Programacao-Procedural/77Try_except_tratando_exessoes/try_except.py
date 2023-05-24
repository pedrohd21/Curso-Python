a = {}
a = []
try:
    print(a[1])
except NameError as erro:
    print('error do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de index ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    print('Seu codigo foi executado com sucesso')

print('Bora continuar')
