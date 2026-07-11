# Primeiro como aqui vai ser o nosso código principal, sabemos uqe aqui precisamos apenas escrever o básico, como puxar funções para criar banco e puxar funções para inciar a interface, por isso podemos criar outros dois arquivos, ou na verda apenas mais um arquivo, um para oa criação dos bancos, e esse fica para acriação de interface, e ele mesmo já vai puxar os outros arquivos para fazer a as funções relacionadas a interface.

import customtkinter as ctk
from banco import criar_tabelas

#Importando as classes para poder visualizar as telas.
from JanelasInterface.CadastroLivros import TelaCadastroLivros
from JanelasInterface.CadastroUusuarios import CadastroTelaUsuarios
from JanelasInterface.emprestimo import TelaEmprestimos
from JanelasInterface.Consulta import TelaConsultas

#1.Priemiro passo é criar as tabelas, aqui etou úcaxndo o que ue fiz dentro do arquivso das tabelas.
criar_tabelas()

#2 Como agora eu já tenho as coisas elacionadas as tabelas onde vamos trabalhar sobre eu posso começar a trabalhar sobre ocmo vamos usar estas tabelas e bamos fazer isso por meio de uma interface, por isso aqui mesmo já posso começar a ver sobre isso

ctk.set_appearance_mode("dark")

#Criando uma subclasse, para deixar tudo dentro dela e nao ficar jogado pelo código sem organizaçãoa agluma.

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #Chamando um método de dentro da classe para dar nome a aba que estamos criando
        self.title("Sistema de Biblioteca")
        self.geometry("500x450")
        titulo = ctk.CTkLabel(self,text=" SISTEMA DA BIBLIOTECA", font = ("Arial", 20, "bold")
                              )
        titulo.pack(pady=30)

        #Criando os botoões para rismos as outras abas do sistema onde ele vai realmetne acontecer. 3. Antes disso então tmeos que criar os arquivos para chamar estas funções que vão estar atribuidas aos bootões
        ctk.CTkButton(self, text="Cadastro de Livros", width= 250, command=lambda : TelaCadastroLivros(self)).pack(pady=10)
        ctk.CTkButton(self, text="Cadastro de Usuários", width=250, command=lambda : CadastroTelaUsuarios(self)).pack(pady=10)

        #Agora é hora de ver sobre os esmpréstimos e agora tenho que ver como que funciona estas coisas com o outro produto
        ctk.CTkButton(self, text="Fazer Empréstimos",width = 250, command=lambda : TelaEmprestimos(self)).pack(pady = 10)

        #Tenho que ver sobre a tela para verificar todos os emprestimos que estão acontecendo, a consulta.
        ctk.CTkButton(self, text="Emprestimos feitos",width = 250, command=lambda : TelaConsultas(self)).pack(pady = 10)
app = App()
app.mainloop()
