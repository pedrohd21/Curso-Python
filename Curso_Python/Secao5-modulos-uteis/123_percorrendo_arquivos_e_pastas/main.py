import os

way_search = input('Digite um caminho: ')
term_search = input('Digite um termo: ')


def format_counter(counter):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if counter < kilo:
        text = 'B'
    elif counter < mega:
        counter /= kilo
        text = 'K'

    elif counter < giga:
        counter /= mega
        text = 'M'

    elif counter < tera:
        counter /= giga
        text = 'G'

    elif counter < peta:
        counter /= tera
        text = 'T'
    else:
        counter /= peta
        text = 'P'

    counter = round(counter, 2)
    return f'{counter}{text}'.replace('.', ',')


counter = 0
for root, directories, files in os.walk(way_search):
    for file in files:
        if term_search in file:
            try:
                counter += 1
                way_complete = os.path.join(root, file)
                # print(way_complete) # mostra o caminho completo
                name_file, ext_file = os.path.splitext(file)
                # print(f'{name_file}{ext_file}') # mostra o nome e o tipo do arquivo
                size = os.path.getsize(way_complete)  # tamanho do arquivo
                # print(size)
                print()
                print('Encontri o arquivo: ', file)
                print('Caminho: ', way_complete)
                print('Nome: ', name_file)
                print('Extensão: ', ext_file)
                print('Tamanho: ', size)
                print('Tamanho formatado: ', format_counter(size))
            except PermissionError as e:
                print('Sem permissões.')
            except FileNotFoundError as e:
                print('Arquivo Não encontrado')
            except Exception as e:
                print('Erro desconhecido: ', e)
print()
print(f'{counter} arquivo(s) encontrado(s).')

