import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conectar():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        # password='cursopython@123',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        conexao.close()


# Add um registro na base de dados
# with conectar() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#         conexao.commit()


# Add varios registro na base de dados
# with conectar() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#
#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('ROSE', 'FIGUEIREDO', 19, 55),
#             ('JOSÉ', 'FIGUEIREDO', 19, 55),
#         ]
#         cursor.executemany(sql, dados)
#         conexao.commit()


# Apaga um registro na base de dados
# with conectar() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6, ))
#         conexao.commit()


# Apaga quantidade determinada de registros
# with conectar() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()


# Apaga Registra entre um range
# with conectar() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10, 12))
#         conexao.commit()

# Atualiza um dados no caso aq, nome
# with conectar() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('JOANA', 5))
#         conexao.commit()


# Mostra a lista de clientes
with conectar() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
