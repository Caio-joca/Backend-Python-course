'''Aqui vamos escrever sobre a classe pessoa'''
# (nome, data_denascimento, endereco,  rg, cpf )
class Pessoa :
    def __init__(self, nome, data_denascimento, endereco, rg, cpf):
        self. nome= nome
        self.data_denascimento = data_denascimento
        self.endereco= endereco
        self.rg= rg
        self.cpf= cpf

#Com a classe principal criada agora podemos criar as subclasses