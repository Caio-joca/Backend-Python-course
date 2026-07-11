'''
Aqui vamos fazer um exercício onde temos que criar uma janela principal com duas opções, uma de cadastro para cadastrar produtos, isso em uma janela Modal e depois temos a segunfa opção onde vai mostrar a lsita de produtos cadastrados.

Para fazer isso é bem simples, mas agora eu vou pegar para aprender as regras do jogo com o jogo j[a feito, e depois vou aplciar para coisas mais avançadas.
'''

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Sistema de Cadastro")
janela.geometry("500x400")

produtos = []


def abrir_cadastro():
    modal = ctk.CTkToplevel(janela)
    modal.title("Cadastro de Produto")
    modal.geometry("400x350")
    modal.grab_set()

    titulo = ctk.CTkLabel(
        modal,
        text="Cadastrar Produto",
        font=("Arial", 24, "bold")
    )
    titulo.pack(pady=25)

    entrada_nome = ctk.CTkEntry(
        modal,
        placeholder_text="Produto",
        width=250
    )
    entrada_nome.pack(pady=10)

    entrada_preco = ctk.CTkEntry(
        modal,
        placeholder_text="Preço",
        width=250
    )
    entrada_preco.pack(pady=10)

    mensagem = ctk.CTkLabel(modal, text="")
    mensagem.pack(pady=10)

    def cadastrar():
        nome = entrada_nome.get()
        preco_texto = entrada_preco.get()

        if nome.strip() == "" or preco_texto.strip() == "":
            mensagem.configure(text="Preencha todos os campos", text_color="red")
            return

        try:
            preco = float(preco_texto)

            if preco <= 0:
                mensagem.configure(text="Preço inválido", text_color="red")
                return

            produto = {
                "nome": nome,
                "preco": preco
            }

            produtos.append(produto)

            mensagem.configure(
                text="Produto cadastrado com sucesso",
                text_color="green"
            )

            entrada_nome.delete(0, "end")
            entrada_preco.delete(0, "end")

        except ValueError:
            mensagem.configure(text="Digite um preço válido", text_color="red")

    botao_cadastrar = ctk.CTkButton(
        modal,
        text="Cadastrar Produto",
        width=250,
        command=cadastrar
    )
    botao_cadastrar.pack(pady=15)


def abrir_lista():
    modal = ctk.CTkToplevel(janela)
    modal.title("Lista de Produtos")
    modal.geometry("450x450")
    modal.grab_set()

    titulo = ctk.CTkLabel(
        modal,
        text="Produtos Cadastrados",
        font=("Arial", 24, "bold")
    )
    titulo.pack(pady=20)

    frame_scroll = ctk.CTkScrollableFrame(
        modal,
        width=350,
        height=300
    )
    frame_scroll.pack(pady=10)

    if len(produtos) == 0:
        aviso = ctk.CTkLabel(
            frame_scroll,
            text="Nenhum produto cadastrado",
            font=("Arial", 16)
        )
        aviso.pack(pady=20)
    else:
        for produto in produtos:
            card = ctk.CTkFrame(
                frame_scroll,
                corner_radius=15
            )
            card.pack(fill="x", padx=10, pady=10)

            nome = ctk.CTkLabel(
                card,
                text=f"Produto: {produto['nome']}",
                font=("Arial", 16, "bold")
            )
            nome.pack(anchor="w", padx=15, pady=(10, 5))

            preco = ctk.CTkLabel(
                card,
                text=f"Preço: R$ {produto['preco']:.2f}",
                font=("Arial", 14)
            )
            preco.pack(anchor="w", padx=15, pady=(0, 10))


titulo_principal = ctk.CTkLabel(
    janela,
    text="Sistema de Cadastro",
    font=("Arial", 28, "bold")
)
titulo_principal.pack(pady=60)

botao_cadastro = ctk.CTkButton(
    janela,
    text="Cadastrar Produto",
    width=220,
    command=abrir_cadastro
)
botao_cadastro.pack(pady=15)

botao_listar = ctk.CTkButton(
    janela,
    text="Listar Produtos",
    width=220,
    command=abrir_lista
)
botao_listar.pack(pady=15)

janela.mainloop()