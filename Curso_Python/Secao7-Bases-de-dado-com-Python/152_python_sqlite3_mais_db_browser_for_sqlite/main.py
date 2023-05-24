import sqlite3


class AgendaDB:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def insert(self, name, telephone):
        consult = 'INSERT OR IGNORE INTO agenda (name, telephone) VALUES (?, ?)'
        self.cursor.execute(consult, (name, telephone))
        self.conn.commit()

    def edit(self, name, telephone, id):
        consult = 'UPDATE OR IGNORE agenda SET name=?, telephone=? WHERE id=?'
        self.cursor.execute(consult, (name, telephone, id))
        self.conn.commit()

    def deleterr(self, id):
        consult = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consult, (id,))
        self.conn.commit()

    def list(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def search(self, valor):
        consult = 'SELECT * FROM agenda WHERE name LIKE ?'
        self.cursor.execute(consult, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')

    # Adicionando
    # agenda.insert('Pedro', '111111')
    # agenda.insert('Maria', '222222')
    # agenda.insert('João', '333333')
    # agenda.insert('Rose', '444444')
    # agenda.insert('Guilherme', '555555')
    # agenda.insert('Fabrício', '666666')
    agenda.insert('Luiz Otávio', 102101)
    agenda.insert('Luiz Felipe', 506852)
    agenda.insert('Ronaldo Luiz', 951753)
    agenda.insert('R. Luiza', 741963)
    agenda.insert('R. Luiza meio', 852456)

    # Edita
    # agenda.edit('Francisco', '121212', 7)

    # Apaga
    # agenda.deleterr(7)

    # Buscar
    agenda.search('luiz')
    # agenda.list()
