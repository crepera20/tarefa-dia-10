import tkinter as tk
from tkinter import messagebox
import os
from clientes_model import Cliente
from cidades_model import Cidade

class ClienteApp:
    def __init__(self, root):
        self.cliente = Cliente()
        self.cidade = Cidade()

        self.root = root
        self.root.title("Cadastro de Clientes")
        self.root.state("zoomed")

        # Frame para centralizar os widgets
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        # Widgets
        self.lblNome = tk.Label(self.frame, text="Nome:", font=("Arial", 18))
        self.lblNome.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txtNome = tk.Entry(self.frame, font=("Arial", 18))
        self.txtNome.grid(row=0, column=1, padx=10, pady=10)

        self.lblTelefone = tk.Label(self.frame, text="Telefone:", font=("Arial", 18))
        self.lblTelefone.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.txtTelefone = tk.Entry(self.frame, font=("Arial", 18))
        self.txtTelefone.grid(row=1, column=1, padx=10, pady=10)

        self.lblEndereco = tk.Label(self.frame, text="Endereço:", font=("Arial", 18))
        self.lblEndereco.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.txtEndereco = tk.Entry(self.frame, font=("Arial", 18))
        self.txtEndereco.grid(row=2, column=1, padx=10, pady=10)

        self.lblCPF = tk.Label(self.frame, text="CPF:", font=("Arial", 18))
        self.lblCPF.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.txtCPF = tk.Entry(self.frame, font=("Arial", 18))
        self.txtCPF.grid(row=3, column=1, padx=10, pady=10)

        self.lblCidade = tk.Label(self.frame, text="Cidade ID:", font=("Arial", 18))
        self.lblCidade.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.txtCidade = tk.Entry(self.frame, font=("Arial", 18))
        self.txtCidade.grid(row=4, column=1, padx=10, pady=10)

        # Botões
        self.btnInserir = tk.Button(self.frame, text="Inserir", command=self.inserir_cliente, font=("Arial", 18))
        self.btnInserir.grid(row=5, column=0, padx=10, pady=10)

        self.btnAlterar = tk.Button(self.frame, text="Alterar", command=self.alterar_cliente, font=("Arial", 18))
        self.btnAlterar.grid(row=5, column=1, padx=10, pady=10)

        self.btnExcluir = tk.Button(self.frame, text="Excluir", command=self.excluir_cliente, font=("Arial", 18))
        self.btnExcluir.grid(row=5, column=2, padx=10, pady=10)

        self.lblMensagem = tk.Label(self.frame, text="", font=("Arial", 18))
        self.lblMensagem.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

    def inserir_cliente(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        endereco = self.txtEndereco.get()
        cpf = self.txtCPF.get()
        cidade_id = self.txtCidade.get()

        if nome and telefone and endereco and cpf and cidade_id:
            self.cliente.inserir(nome, telefone, endereco, cpf, cidade_id)
            messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

    def alterar_cliente(self):
        # Implementar a lógica de alteração
        pass

    def excluir_cliente(self):
        # Implementar a lógica de exclusão
        pass

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteApp(root)
    root.mainloop()
