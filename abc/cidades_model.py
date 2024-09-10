from Banco import Banco

class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.banco = Banco()

    def salvar(self):
        self.banco.inserir_cidade(self.nome)

    @classmethod
    def listar(cls):
        banco = Banco()
        cidades = banco.listar_cidades()
        banco.fechar_conexao()
        return cidades
