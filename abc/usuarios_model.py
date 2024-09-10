from Banco import Banco

class Usuario:
    def __init__(self):
        self.banco = Banco()

    def inserir(self, nome, telefone, email, usuario, senha):
        try:
            cursor = self.banco.conexao.cursor()
            cursor.execute('''
                INSERT INTO usuarios (nome, telefone, email, usuario, senha)
                VALUES (?, ?, ?, ?, ?)
            ''', (nome, telefone, email, usuario, senha))
            self.banco.conexao.commit()
            print("Usuário inserido com sucesso!")  # Mensagem de depuração
        except Exception as e:
            print(f"Erro ao inserir no banco de dados: {e}")  # Mensagem de depuração para erro

    def alterar(self, idUsuario, nome, telefone, email, usuario, senha):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE usuarios SET nome=?, telefone=?, email=?, usuario=?, senha=?
            WHERE idUsuario=?
        ''', (nome, telefone, email, usuario, senha, idUsuario))
        self.banco.conexao.commit()

    def excluir(self, idUsuario):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM usuarios WHERE idUsuario=?', (idUsuario,))
        self.banco.conexao.commit()

    def buscar(self, idUsuario):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE idUsuario=?', (idUsuario,))
        resultado = cursor.fetchone()
        return resultado