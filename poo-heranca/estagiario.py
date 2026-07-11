#aqui vamos criar a sublcasse estagiário,
# precisando de valor da bolsa estágio, data de inicio estágio, código estágiário, código aluno

from pessoa import Pessoa

class Estagiario (Pessoa):
    contador=1
    def __init__(self, nome, data_denascimento, endereco, rg, cpf, codigodoaluno, bolsa_estagio, inicio_estagio):
        super().__init__(nome, data_denascimento, endereco, rg, cpf)
        self.codigodoaluno = codigodoaluno
        self.bolsa_estagio = bolsa_estagio
        self.inicio_estagio = inicio_estagio

        self.codigoestagiario= Estagiario.contador
        Estagiario.contador+=1
       


