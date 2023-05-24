"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv


with open('clientes.csv', 'r') as file:
    dice = [x for x in csv.DictReader(file)]
    # # dice = csv.reader(file)
    # for dices in dice:
    #     print(dices['Nome'])

with open('cliente2.csv', 'w') as file:
    write = csv.writer(
        file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )
    keys = dice[0].keys()
    keys = list(keys)
    write.writerow(
        [
            keys[0],
            keys[1],
            keys[2],
            keys[3],
        ]
    )

    for dices in dice:
        write.writerow(
            [
                dices['Nome'],
                dices['Sobrenome'],
                dices['E-mail'],
                dices['Telefone'],
            ]
        )

