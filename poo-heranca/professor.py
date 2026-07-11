#aqui vamos fazer a criaçõa da sublcasse profesor
from pessoa import Pessoa

#ele precisa de código de funcinario, discilpinas, data de admissão
class Professor (Pessoa):
    contador=1
    def __init__(self, nome, data_denascimento, endereco, rg, cpf, disciplinas, data_admissao):
        super().__init__(nome, data_denascimento, endereco, rg, cpf)
        self.disciplinas= disciplinas 
        self.data_admissao= data_admissao

        self.codigo_professor= Professor.contador
        Professor.contador+=1


