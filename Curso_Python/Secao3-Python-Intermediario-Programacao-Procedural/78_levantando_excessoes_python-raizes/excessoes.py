# começo codigo
# def divide(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error:
#         print('log:', error)
#         raise
#
#
# try:
#     print(divide(2, 0))
# except ZeroDivisionError as error:
#     print('error')


# Começo codigo


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0")
    return n1 / n2


try:
    print(divide(5, 0))
except ValueError as error:
    print('Voçe esta tentando dividir por 0.')
    print('Log:', error)