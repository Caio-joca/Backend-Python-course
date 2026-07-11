import customtkinter as ctk
from banco import conectar

class TelaConsultas(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Livros Emprestados")
        self.geometry("900x500")
        self.grab_set()
        frame = ctk.CTkScrollableFrame(self)
        frame.pack(fill = "both", expand = True)
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
        """
        SELECT
            usuarios.nome,
            livros.titulo,
            emprestimos.data_emprestimo,
            emprestimos.data_devolucao,
            emprestimos.status
        FROM emprestimos
        INNER JOIN usuarios
        ON usuarios.id = emprestimos.usuario_id
        INNER JOIN livros
        ON livros.id = emprestimos.livro_id
        """)

        dados = cursor.fetchall()
        conn.close()
        for item in dados:
            texto = f"""
Usuário : {item[0]}
Livro : {item[1]}
Empréstimo: {item[2]}
Devolução: {item[3]}
Status: {item[4]}
                    """
            ctk.CTkLabel(frame, text = texto, anchor = "w", justify = "left").pack(fill = "x", padx = 10, pady =10)