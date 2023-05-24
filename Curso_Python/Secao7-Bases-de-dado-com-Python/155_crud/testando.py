import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conectar():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        db='comandos',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()

with conectar() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM comandos_uteis')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)