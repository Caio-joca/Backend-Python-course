#Aqui vamos fazer o código para atender o cadastro de usuários. Ainda não consigo fazer isso da minha cabeça.

import customtkinter as ctk
from banco import conectar

#Tenho que criar agora 

class CadastroTelaUsuarios(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        #O que vai ser printado para o suuários na interface
        self.title("Cadastro de Usuários")
        self.geometry("600x400")
        self.grab_set()

        #O que vai ser printado para que ele possa mandar dadso para o banco de dados.
        ctk.CTkLabel(self, text = "Nome").pack()
        self.nome = ctk.CTkEntry(self, width = 400)
        self.nome.pack(pady = 5)
        
        ctk.CTkLabel(self, text = "CPF").pack()
        self.cpf = ctk.CTkEntry(self, width = 400)
        self.cpf.pack(pady = 5)

        ctk.CTkLabel(self, text = "Telefone").pack()
        self.telefone = ctk.CTkEntry(self, width = 400)
        self.telefone.pack(pady = 5)

        ctk.CTkLabel(self, text = "Email").pack()
        self.email = ctk.CTkEntry(self, width = 400)
        self.email.pack(pady = 5)

        #Criando botão agora para poder salvar os dados dentro do vanco de dados
        ctk.CTkButton(self, text = "Salva", command = self.salvar).pack(pady = 20)

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
        """
        INSERT INTO usuarios
        (nome, cpf, telefone, email)
        VALUES (?, ?, ?, ?)
        """, (
            self.nome.get(),
            self.cpf.get(),
            self.telefone.get(),
            self.email.get()
        ))
        conn.commit()
        conn.close()
        self.destroy()




