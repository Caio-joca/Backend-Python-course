#Aqui vou fazer o código sobre os emprestimos, relacionando as duas tabelas

import customtkinter as ctk
from banco import conectar
from datetime import datetime, timedelta

class TelaEmprestimos(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Empréstimos")
        self.geometry("600x300")
        self.grab_set()
        conn = conectar()
        cursor = conn.cursor()

        #Pegando os dados de suusarios de dentro da tabela de banco de dados ususarios
        cursor.execute("SELECT id, nome FROM usuarios")
        usuarios = cursor.fetchall()

        #Pegandos dados de dentro da taela de livros, para poder fazer a ssosiação de dados entre as duas tabelas.
        cursor.execute(
        """
        SELECT id, titulo
        FROM livros
        WHERE quantidade > 0    
        """
        )
        livros = cursor.fetchall()
        conn.close()

        #Transformando dados em um dicionários para ficar mais fácil de se visualizar
        self.usuarios = {nome: id
            for id, nome in usuarios
        }
        self.livros = {titulo: id
            for id, titulo in livros
        }


        #Criando a capacidade de se ter um tipo de capacidade da interface, para abriruma lista e pdoer selecionar qual lvro ou pessoa queremos fazer a relação de empréstimo.
        ctk.CTkLabel(self, text = " Usuário").pack()
        self.combo_usuario = ctk.CTkComboBox(self,
            values = list(self.usuarios.keys())
        )
        self.combo_usuario.pack(pady = 10)

        self.combo_livro = ctk.CTkComboBox(self,
            values=list(self.livros.keys())
        )
        self.combo_livro.pack(pady=10)

        #Criando botão para poder salvar os dados dentro do banco de dados de empréstimos feitos.
        ctk.CTkButton(self,text="Emprestar",command=self.emprestar
        ).pack(pady=20)

    def emprestar(self):
        usuario = self.usuarios[self.combo_usuario.get()]
        livro = self.livros[self.combo_livro.get()]

        hoje = datetime.now()
        devolucao = hoje + timedelta(days = 7)
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
        """
        INSERT INTO emprestimos
        (usuario_id, livro_id,
        data_emprestimo,
        data_devolucao,
        status)
        VALUES (?,?,?,?,?)
        """, (
            usuario,
            livro,
            hoje.strftime("%d/%m/%Y"),
            devolucao.strftime("%d/%m/%Y"),
            "Emprestado"
        ))

        cursor.execute("""
        UPDATE livros
        SET quantidade = quantidade - 1
        WHERE id=?
        """,(livro,))
        conn.commit()
        conn.close()
        self.destroy()