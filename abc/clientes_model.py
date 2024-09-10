from banco import Banco

class Cliente:
    def __init__(self):
        self.banco = Banco()

    def inserir(self, nome, telefone, endereco, cpf, cidade_id):  # Usando cidade_id como referência
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            INSERT INTO cliente (nome, telefone, endereco, cpf, cidade)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, telefone, endereco, cpf, cidade_id))
        self.banco.conexao.commit()

    def alterar(self, idcli, nome, telefone, endereco, cpf, cidade_id):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE cliente SET nome=?, telefone=?, endereco=?, cpf=?, cidade=?
            WHERE idcli=?
        ''', (nome, telefone, endereco, cpf, cidade_id, idcli))
        self.banco.conexao.commit()

    def excluir(self, idcli):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM cliente WHERE idcli=?', (idcli,))
        self.banco.conexao.commit()

    def buscar(self, idcli):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM cliente WHERE idcli=?', (idcli,))
        return cursor.fetchone()
