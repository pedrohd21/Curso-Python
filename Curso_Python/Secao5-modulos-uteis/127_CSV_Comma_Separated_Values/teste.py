import csv

with open('aaa.csv', 'r') as file:
    dice = csv.reader(file)
    for dices in dice:
        print(dices)