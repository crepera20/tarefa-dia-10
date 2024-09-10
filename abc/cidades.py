import tkinter as tk
from tkinter import messagebox
from cidades_model import Cidade

class CidadeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Cidades")

        self.label = tk.Label(root, text="Gerenciador de Cidades", font=("Arial", 16))
        self.label.pack(pady=10)

        self.nome_var = tk.StringVar()

        self.entry = tk.Entry(root, textvariable=self.nome_var, width=30)
        self.entry.pack(pady=5)
        self.entry.insert(0, "Digite o nome da cidade")

        self.add_button = tk.Button(root, text="Adicionar Cidade", command=self.adicionar_cidade)
        self.add_button.pack(pady=5)

        self.list_button = tk.Button(root, text="Listar Cidades", command=self.listar_cidades)
        self.list_button.pack(pady=5)

        self.list_box = tk.Listbox(root, width=50)
        self.list_box.pack(pady=10)

    def adicionar_cidade(self):
        nome = self.nome_var.get()
        if nome:
            cidade = Cidade(nome)
            cidade.salvar()
            messagebox.showinfo("Sucesso", f"Cidade '{nome}' adicionada com sucesso.")
            self.nome_var.set("")  # Limpa o campo de entrada
        else:
            messagebox.showwarning("Atenção", "Por favor, insira um nome para a cidade.")

    def listar_cidades(self):
        self.list_box.delete(0, tk.END)  # Limpa a lista antes de listar
        cidades = Cidade.listar()
        for cidade in cidades:
            self.list_box.insert(tk.END, cidade[1])  # Adiciona o nome da cidade à lista

if __name__ == "__main__":
    root = tk.Tk()
    app = CidadeApp(root)
    root.mainloop()
