#Aqui vamos criar a janela que vai ser chamada quando a função para cadastrar livros for chamada na interface da janela principal

import customtkinter as ctk
from banco import conectar

#Como vamos chamar apenas uma função de dento deste arquvis, temos que deixar tudo dentro d e uma classe, para deixar tudo organiado, portanto lá no aruqivos vamos estar chamando na verdade a classe, que vai printar tudoq ue tem de dentro dela.

class TelaCadastroLivros(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cadastro de Livros")
        self.geometry("600x400")
        #Método para apenas esta janela de todas as janelas abertasfuncionarem
        self.grab_set()
        
        #Criando bloco de texto para falar que tem que escrevr o título
        ctk.CTkLabel(self, text="Título").pack()
        #Criando variável para guardar o título com base no que tem escrito dentro do bloco de escrita
        self.titulo = ctk.CTkEntry(self, width=400)
        #Printando essa variável com .pack
        self.titulo.pack(pady = 5)

        #Criando variaavel para printar outra coisa na tela. e depois uma varia´vel para escrever coisa na tela para enviar ao banco de dados.
        ctk.CTkLabel(self, text="Autor").pack()
        self.autor = ctk.CTkEntry(self, width = 400)
        self.autor.pack(pady = 5)

        #Variavelagora para o genero
        ctk.CTkLabel(self, text="Gênero").pack()
        self.genero = ctk.CTkEntry(self, width=400)
        self.genero.pack(pady=5)

        #Variavel para as páginas
        ctk.CTkLabel(self, text="Páginas").pack()
        self.paginas = ctk.CTkEntry(self, width=400)
        self.paginas.pack(pady=5)

        #Variável para as quatidades de livros
        ctk.CTkLabel(self, text = " Quantidade").pack()
        self.quantidade = ctk.CTkEntry(self, width = 400)
        self.quantidade.pack(pady = 5)

        ctk.CTkButton(self, text = "Salvar", command=self.salvar).pack(pady=20)

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO livros
        (titulo, autor, genero, paginas, quantidade)
        VALUES (?,?,?,?,?)
        """, (
            self.titulo.get(),
            self.autor.get(),
            self.genero.get(),
            self.paginas.get(),
            self.quantidade.get(),
        ))
        conn.commit()
        conn.close()
        self.destroy()

        #Agora que criei a interface para mostrar as funções para conseguir ecessar e alterar o bacno, eu posso chamar ela dentro da função pricnipla, ou seja, toda vez que eu clicar no botão de cadastro de livros ess função vai ser chamada e a páginas para abrir o cadastro de banco de livros vai ser aberto.

