from random import randint


def buzz(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        return 'FizzBuzz'
    if n1 % 3 == 0:
        return 'Fizz'
    if n1 % 5 == 0:
        return 'Buzz'
    return n1


for c in range(0, 20):
    print(buzz(randint(0, 100)))
