import customtkinter as ctk

# Aparência
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# Janela principal
janela = ctk.CTk()
janela.title("Calculadora de Soma")
janela.geometry("400x300")

# ---------- FUNÇÃO ----------
def somar():

    # Pegando os valores digitados
    numero1 = entrada_num1.get()
    numero2 = entrada_num2.get()

    try:
        numero1 = float(numero1)
        numero2 = float(numero2)

        resultado = numero1 + numero2

        # Altera o texto do label
        texto_resultado.configure(
            text=f"Resultado: {resultado}"
        )

    except ValueError:
        texto_resultado.configure(
            text="Digite apenas números"
        )

# ---------- TÍTULO ----------
titulo = ctk.CTkLabel(
    janela,
    text="Calculadora",
    font=("Arial", 24)
)

titulo.pack(pady=20)

# ---------- PRIMEIRO NÚMERO ----------
entrada_num1 = ctk.CTkEntry(
    janela,
    placeholder_text="Digite o primeiro número"
)

entrada_num1.pack(pady=10)

# ---------- SEGUNDO NÚMERO ----------
entrada_num2 = ctk.CTkEntry(
    janela,
    placeholder_text="Digite o segundo número"
)

entrada_num2.pack(pady=10)

# ---------- BOTÃO ----------
botao_somar = ctk.CTkButton(
    janela,
    text="Somar",
    command=somar
)

botao_somar.pack(pady=20)

# ---------- RESULTADO ----------
texto_resultado = ctk.CTkLabel(
    janela,
    text="Resultado aparecerá aqui",
    font=("Arial", 18)
)

texto_resultado.pack(pady=10)

# ---------- LOOP PRINCIPAL ----------
janela.mainloop()