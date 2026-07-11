import customtkinter as ctk
from Bancodedados import inserir_veiculo, buscar_veiculos


def iniciar_interface():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    janela = ctk.CTk()
    janela.title("Sistema de Veículos")
    janela.geometry("430x500")

    def cadastrar():
        placa = entrada_placa.get()
        proprietario = entrada_proprietario.get()
        marca = entrada_marca.get()
        modelo = entrada_modelo.get()

        if (
            placa.strip() == "" or
            proprietario.strip() == "" or
            marca.strip() == "" or
            modelo.strip() == ""
        ):
            mensagem.configure(
                text="Preencha todos os campos",
                text_color="red"
            )
            return

        inserir_veiculo(placa, proprietario, marca, modelo)

        mensagem.configure(
            text="Veículo cadastrado com sucesso",
            text_color="green"
        )

        entrada_placa.delete(0, "end")
        entrada_proprietario.delete(0, "end")
        entrada_marca.delete(0, "end")
        entrada_modelo.delete(0, "end")

    def abrir_lista():
        veiculos = buscar_veiculos()

        modal = ctk.CTkToplevel(janela)
        modal.title("Lista de Veículos")
        modal.geometry("700x400")
        modal.grab_set()

        titulo_modal = ctk.CTkLabel(
            modal,
            text="Veículos Cadastrados",
            font=("Arial", 24, "bold")
        )
        titulo_modal.pack(pady=20)

        frame_scroll = ctk.CTkScrollableFrame(
            modal,
            width=650,
            height=280
        )
        frame_scroll.pack(pady=10)

        if len(veiculos) == 0:
            aviso = ctk.CTkLabel(
                frame_scroll,
                text="Nenhum veículo cadastrado",
                font=("Arial", 16)
            )
            aviso.pack(pady=20)
            return

        for veiculo in veiculos:
            texto = (
                f"ID: {veiculo[0]} | "
                f"Placa: {veiculo[1]} | "
                f"Proprietário: {veiculo[2]} | "
                f"Marca: {veiculo[3]} | "
                f"Modelo: {veiculo[4]}"
            )

            label = ctk.CTkLabel(
                frame_scroll,
                text=texto,
                font=("Arial", 14),
                anchor="w"
            )
            label.pack(fill="x", padx=10, pady=5)

    titulo = ctk.CTkLabel(
        janela,
        text="Cadastro de Veículos",
        font=("Arial", 24, "bold")
    )
    titulo.pack(pady=15)

    entrada_placa = ctk.CTkEntry(
        janela,
        placeholder_text="Placa",
        width=300
    )
    entrada_placa.pack(pady=5)

    entrada_proprietario = ctk.CTkEntry(
        janela,
        placeholder_text="Proprietário",
        width=300
    )
    entrada_proprietario.pack(pady=5)

    entrada_marca = ctk.CTkEntry(
        janela,
        placeholder_text="Marca",
        width=300
    )
    entrada_marca.pack(pady=5)

    entrada_modelo = ctk.CTkEntry(
        janela,
        placeholder_text="Modelo",
        width=300
    )
    entrada_modelo.pack(pady=5)

    botao_cadastrar = ctk.CTkButton(
        janela,
        text="Cadastrar Veículo",
        command=cadastrar,
        width=300
    )
    botao_cadastrar.pack(pady=10)

    botao_listar = ctk.CTkButton(
        janela,
        text="Listar Veículos",
        command=abrir_lista,
        width=300
    )
    botao_listar.pack(pady=5)

    mensagem = ctk.CTkLabel(
        janela,
        text=""
    )
    mensagem.pack(pady=10)

    janela.mainloop()