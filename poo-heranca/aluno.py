from pessoa import Pessoa

#aqui vamos criar a subclasse alunos, essa clase tera aditivos de data de ingresso, código aluno, curso
#semestre, e valor_mensalidade

class Alunos(Pessoa):
    contador=1

                #já que ou utilizar uma variável interna da classe, não preciso recer um código de aluno
    def __init__(self, nome, data_denascimento, endereco, rg, cpf, data_ingressao, curso, semestre, valor_mensalidade):
        super().__init__(nome, data_denascimento, endereco, rg, cpf)
        self.data_ingressao=data_ingressao
        self.curso=curso
        self.semestre= semestre
        self.valor_mensalidade = valor_mensalidade

        self.codigo = Alunos.contador
        Alunos.contador+=1

