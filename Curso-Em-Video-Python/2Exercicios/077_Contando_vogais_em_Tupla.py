palavras = ('Agua', 'Cruzeiro', 'Rap', 'Know', 'Lapis', 'Naruto', 'Itachi', 'Jiraia', 'Python', 'Programar', 'Futuro')
for n in palavras:
    print(f'\nNa palavra {n.upper()} temos ', end='')
    for letra in n:
        if letra.upper() in 'AEIOU':
            print(letra, end='')