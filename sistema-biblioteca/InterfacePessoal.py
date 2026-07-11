'''Aqui vamos criar a interface para que o usuário consiga mexer via uma interface'''

import customtkinter as ctk
from BancoBilioteca import inserir_livros, BuscarLivros, BuscarLivroPorId, alterar_livro, excluir_livro


def iniciar_interface():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    janela = ctk.CTk()
    janela.title("Sistema de Biblioteca")
    janela.geometry("430x300")

    def abrir_cadastro():
        modal = ctk.CTkToplevel(janela)
        modal.title("Cadastrar Livro")
        modal.geometry("430x600")
        modal.grab_set()

        titulo_modal = ctk.CTkLabel(
            modal,
            text="Cadastro de Livro",
            font=("Arial", 24, "bold")
        )
        titulo_modal.pack(pady=20)

        entrada_titulo = ctk.CTkEntry(
            modal,
            placeholder_text="Título",
            width=350
        )
        entrada_titulo.pack(pady=8)

        entrada_autor = ctk.CTkEntry(
            modal,
            placeholder_text="Autor",
            width=350
        )
        entrada_autor.pack(pady=8)

        entrada_genero = ctk.CTkEntry(
            modal,
            placeholder_text="Gênero",
            width=350
        )
        entrada_genero.pack(pady=8)

        entrada_paginas = ctk.CTkEntry(
            modal,
            placeholder_text="Número de páginas",
            width=350
        )
        entrada_paginas.pack(pady=8)

        label_resumo = ctk.CTkLabel(
            modal,
            text="Resumo"
        )
        label_resumo.pack(pady=(15, 5))

        entrada_resumo = ctk.CTkTextbox(
            modal,
            width=350,
            height=150
        )
        entrada_resumo.pack(pady=8)

        mensagem = ctk.CTkLabel(
            modal,
            text=""
        )
        mensagem.pack(pady=8)

        def cadastrar():
            titulo = entrada_titulo.get()
            autor = entrada_autor.get()
            genero = entrada_genero.get()
            paginas = entrada_paginas.get()
            resumo = entrada_resumo.get("0.0", "end")

            if (
                titulo.strip() == "" or
                autor.strip() == "" or
                genero.strip() == "" or
                paginas.strip() == "" or
                resumo.strip() == ""
            ):
                mensagem.configure(
                    text="Preencha todos os campos",
                    text_color="red"
                )
                return

            try:
                paginas = int(paginas)

                if paginas <= 0:
                    mensagem.configure(
                        text="O número de páginas deve ser maior que zero",
                        text_color="red"
                    )
                    return

            except ValueError:
                mensagem.configure(
                    text="Digite um número válido em páginas",
                    text_color="red"
                )
                return

            inserir_livros(titulo, autor, genero, paginas, resumo)

            mensagem.configure(
                text="Livro cadastrado com sucesso",
                text_color="green"
            )

            entrada_titulo.delete(0, "end")
            entrada_autor.delete(0, "end")
            entrada_genero.delete(0, "end")
            entrada_paginas.delete(0, "end")
            entrada_resumo.delete("0.0", "end")

        botao_salvar = ctk.CTkButton(
            modal,
            text="Salvar",
            command=cadastrar,
            width=200
        )
        botao_salvar.pack(pady=15)

    def abrir_alteracao(id_livro, atualizar_lista):
        livro = BuscarLivroPorId(id_livro)

        if livro is None:
            return

        modal = ctk.CTkToplevel(janela)
        modal.title("Alterar Livro")
        modal.geometry("430x600")
        modal.grab_set()

        titulo_modal = ctk.CTkLabel(
            modal,
            text="Alterar Livro",
            font=("Arial", 24, "bold")
        )
        titulo_modal.pack(pady=20)

        entrada_titulo = ctk.CTkEntry(modal, placeholder_text="Título", width=350)
        entrada_titulo.pack(pady=8)
        entrada_titulo.insert(0, livro[1])

        entrada_autor = ctk.CTkEntry(modal, placeholder_text="Autor", width=350)
        entrada_autor.pack(pady=8)
        entrada_autor.insert(0, livro[2])

        entrada_genero = ctk.CTkEntry(modal, placeholder_text="Gênero", width=350)
        entrada_genero.pack(pady=8)
        entrada_genero.insert(0, livro[3])

        entrada_paginas = ctk.CTkEntry(modal, placeholder_text="Número de páginas", width=350)
        entrada_paginas.pack(pady=8)
        entrada_paginas.insert(0, livro[4])

        label_resumo = ctk.CTkLabel(
            modal,
            text="Resumo"
        )
        label_resumo.pack(pady=(15, 5))

        entrada_resumo = ctk.CTkTextbox(
            modal,
            width=350,
            height=150
        )
        entrada_resumo.pack(pady=8)
        entrada_resumo.insert("0.0", livro[5])

        mensagem = ctk.CTkLabel(
            modal,
            text=""
        )
        mensagem.pack(pady=8)

        def salvar_alteracao():
            titulo = entrada_titulo.get()
            autor = entrada_autor.get()
            genero = entrada_genero.get()
            paginas = entrada_paginas.get()
            resumo = entrada_resumo.get("0.0", "end")

            if (
                titulo.strip() == "" or
                autor.strip() == "" or
                genero.strip() == "" or
                paginas.strip() == "" or
                resumo.strip() == ""
            ):
                mensagem.configure(
                    text="Preencha todos os campos",
                    text_color="red"
                )
                return

            try:
                paginas = int(paginas)

                if paginas <= 0:
                    mensagem.configure(
                        text="O número de páginas deve ser maior que zero",
                        text_color="red"
                    )
                    return

            except ValueError:
                mensagem.configure(
                    text="Digite um número válido em páginas",
                    text_color="red"
                )
                return

            alterar_livro(id_livro, titulo, autor, genero, paginas, resumo)

            mensagem.configure(
                text="Livro alterado com sucesso",
                text_color="green"
            )

            atualizar_lista()

        botao_salvar = ctk.CTkButton(
            modal,
            text="Salvar Alteração",
            command=salvar_alteracao,
            width=200
        )
        botao_salvar.pack(pady=15)

    def abrir_lista():
        modal = ctk.CTkToplevel(janela)
        modal.title("Lista de Livros")
        modal.geometry("800x500")
        modal.grab_set()

        titulo_modal = ctk.CTkLabel(
            modal,
            text="Livros Cadastrados",
            font=("Arial", 24, "bold")
        )
        titulo_modal.pack(pady=20)

        frame_scroll = ctk.CTkScrollableFrame(
            modal,
            width=740,
            height=360
        )
        frame_scroll.pack(pady=10)

        def carregar_dados():
            for widget in frame_scroll.winfo_children():
                widget.destroy()

            livros = BuscarLivros()

            if len(livros) == 0:
                aviso = ctk.CTkLabel(
                    frame_scroll,
                    text="Nenhum livro cadastrado",
                    font=("Arial", 16)
                )
                aviso.pack(pady=20)
                return

            for livro in livros:
                id_livro = livro[0]
                titulo = livro[1]
                autor = livro[2]
                genero = livro[3]
                paginas = livro[4]
                resumo = livro[5]

                linha = ctk.CTkFrame(
                    frame_scroll
                )
                linha.pack(
                    fill="x",
                    padx=10,
                    pady=10
                )

                texto = (
                    f"Título: {titulo}\n"
                    f"Autor: {autor}\n"
                    f"Gênero: {genero}\n"
                    f"Páginas: {paginas}\n"
                    f"Resumo: {resumo.strip()}"
                )

                label = ctk.CTkLabel(
                    linha,
                    text=texto,
                    font=("Arial", 14),
                    justify="left",
                    anchor="w"
                )
                label.grid(
                    row=0,
                    column=0,
                    padx=15,
                    pady=10,
                    sticky="w"
                )

                botao_alterar = ctk.CTkButton(
                    linha,
                    text="Alterar",
                    width=100,
                    command=lambda id_atual=id_livro: abrir_alteracao(id_atual, carregar_dados)
                )
                botao_alterar.grid(
                    row=0,
                    column=1,
                    padx=10,
                    pady=10
                )

                def excluir_atual(id_atual=id_livro):
                    excluir_livro(id_atual)
                    carregar_dados()

                botao_excluir = ctk.CTkButton(
                    linha,
                    text="Excluir",
                    width=100,
                    fg_color="red",
                    hover_color="darkred",
                    command=excluir_atual
                )
                botao_excluir.grid(
                    row=0,
                    column=2,
                    padx=10,
                    pady=10
                )

        carregar_dados()

    titulo_principal = ctk.CTkLabel(
        janela,
        text="Sistema de Livros",
        font=("Arial", 24, "bold")
    )
    titulo_principal.pack(pady=50)

    botao_cadastrar = ctk.CTkButton(
        janela,
        text="Cadastrar Livro",
        command=abrir_cadastro,
        width=250
    )
    botao_cadastrar.pack(pady=10)

    botao_listar = ctk.CTkButton(
        janela,
        text="Listar Livros",
        command=abrir_lista,
        width=250
    )
    botao_listar.pack(pady=10)

    janela.mainloop()