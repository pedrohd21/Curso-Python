import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# Cria o banco de dados
# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

# Adiciona valores no banco de dados
# cursor.execute('INSERT INTO clientes(nome, peso) VALUES (?, ?)', ('Maria', 50)) # Criar de um jeito seguro
# cursor.execute(
#                'INSERT INTO clientes(nome, peso) VALUES (:nome, :peso)',
#                {'nome': 'Joãozinho', 'peso': 25}
# )
# cursor.execute( # adiciona um id, e adiciona mais valores no banco
#                 'INSERT INTO clientes(id, nome, peso) VALUES (:id, :nome, :peso)',
#                {'id': None, 'nome': 'Daniel', 'peso': 113}
# )
#
# conexao.commit()

# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',  # Atualiza o banco de dados
# cursor.execute('DELETE FROM clientes WHERE id=:id',  # Vai apagar
#                {'id': 2})
# conexao.commit()

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',
               {'peso': 50})

for linha in cursor.fetchall():
    nome, peso = linha

    print(nome, peso)

cursor.close()
conexao.close()

