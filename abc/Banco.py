import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('cidades.db')
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cidades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        ''')
        self.conexao.commit()

    def inserir_cidade(self, nome):
        self.cursor.execute('INSERT INTO cidades (nome) VALUES (?)', (nome,))
        self.conexao.commit()

    def listar_cidades(self):
        self.cursor.execute('SELECT * FROM cidades')
        return self.cursor.fetchall()

    def fechar_conexao(self):
        self.conexao.close()
