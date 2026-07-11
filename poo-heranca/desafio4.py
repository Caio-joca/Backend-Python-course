import os

from pessoa import Pessoa
from aluno import Alunos
from estagiario import Estagiario
from professor import Professor

'''como o ultimo exercício envolvenco herança, preciso criar uma classe pai , a partir da informalção
desse vez, de 3 variáveis, professor, aluno e estágiário. a classe pai tera nome de pessoa, já que une as 3

analisando as variáveis, posso dizer que  tenho que criar um classe pessoa com os elementos
 (nome, data_denascimento, endereco,  rg, cpf )'''

'''Com as classes criadas agora podemos avançar no códogio para o requisitado'''
lista_de_alunos = []
def adicionar_alunos():
    quantidade = int(input('escreva quantos alunos voce quer adicionar'))
    os.system("cls")

    for i in range(quantidade) :
        nome = input('escreva o nome :')
        cpf = input ('escreva o cpf : ')
        rg = input ('escreva o rg : ')
        endereco = input ('escreva o endereço : ')
        datanascimento = input('escreva a data de nascimento como xx/xx/xx : ')
        curso = input('escreva o curso dele')
        dataingressao = input('escreva a data de ingressão como xx/xx/xx : ')
        semestre = input('escreva o semestre emq ue o aluno se encontra')
        mensalidade= input('escreva sua mensalidade')

        input('pressione enter para continuar')

        objectoaluno = Alunos(nome, datanascimento, endereco, rg, cpf, dataingressao, curso, semestre, mensalidade)
        lista_de_alunos.append(objectoaluno)
        print('aluno cadastrado com sucesso \n')

def listar_alunos(alunoslistados):
    if alunoslistados == 0:
        print('sem alunos registrados')
    else :
        for i in alunoslistados :
            print(
                f"\nCodigo do aluno: {i.codigo}\n"
                f"\nNome: {i.nome}\n"
                f"CPF: {i.cpf}\n"
                f"RG: {i.rg}\n"
                f"Endereço: {i.endereco}\n"
                f"Data de nascimento: {i.data_denascimento}\n"
                f"Curso: {i.curso}\n"
                f"Data de ingressão: {i.data_ingressao}\n"
                f"Semestre: {i.semestre}\n"
                f"Mensalidade: {i.valor_mensalidade}\n"
                                    )

'''Funções ligadas ao professor'''
lista_de_professores = []
def adicionar_profssores():
    quantidade = int(input('escreva quantos professores voce quer adicionar'))
    os.system("cls")

    for i in range(quantidade) :
        nome = input('escreva o nome :')
        cpf = input ('escreva o cpf : ')
        rg = input ('escreva o rg : ')
        endereco = input ('escreva o endereço : ')
        datanascimento = input('escreva a data de nascimento como xx/xx/xx : ')
        disciplinas = input('escreva sua disciplina')
        admissao = input('escreva a data de admissão como xx/xx/xx : ')

        input('pressione enter para continuar')

        objectprofessor = Professor(nome, datanascimento, endereco, rg, cpf, disciplinas, admissao)
        lista_de_professores.append(objectprofessor)
        print('professor cadastrado com sucesso \n')

def listar_professores(professoreslistados):
    if professoreslistados == 0:
        print('sem alunos registrados')
    else :
        for i in professoreslistados :
            print(
                f"\nCodigo do professor: {i.codigo_professor}\n"
                f"Nome: {i.nome}\n"
                f"CPF: {i.cpf}\n"
                f"RG: {i.rg}\n"
                f"Endereço: {i.endereco}\n"
                f"Data de nascimento: {i.data_denascimento}\n"
                f"Curso: {i.disciplinas}\n"
                f"Data de ingressão: {i.data_admissao}\n"
                                    )



'''Funções para estagiários'''
lista_de_estagiarios = []
def adicionar_estagiarios():
    quantidade = int(input('escreva quantos estagiarios voce quer adicionar'))
    os.system("cls")

    for i in range(quantidade) :
        nome = input('escreva o nome :')
        cpf = input ('escreva o cpf : ')
        rg = input ('escreva o rg : ')
        endereco = input ('escreva o endereço : ')
        datanascimento = input('escreva a data de nascimento como xx/xx/xx : ')
        codigoaluno= input('escreva o código do aluno : ')
        bolsa = input('escreva o vlaor da bolsa estágio : ')
        iniciodoestagio = input('escreva a data de inicio do estágio como xx/xx/xx : ')

        input('pressione enter para continuar')
        
        objectestagiario = Estagiario(nome, datanascimento, endereco, rg, cpf, codigoaluno, bolsa, iniciodoestagio)
        lista_de_estagiarios.append(objectestagiario)
        print('Estagiário cadastrado com sucesso \n')

def listar_estagiarios(estagiarioslistados):
    if estagiarioslistados == 0:
        print('sem alunos registrados')
    else :
        for i in estagiarioslistados :
            print(
                f"\nCódigo do estagiario: {i.codigoestagiario}\n"
                f"Nome: {i.nome}\n"
                f"CPF: {i.cpf}\n"
                f"RG: {i.rg}\n"
                f"Endereço: {i.endereco}\n"
                f"Data de nascimento: {i.data_denascimento}\n"
                f"Código do aluno: {i.codigodoaluno}\n"
                f"valor da bolsa estágio: {i.bolsa_estagio}\n"
                f"Data de inicio do estágio: {i.inicio_estagio}\n"
                                    )
while True :
    op = int(input(
        "\n1 - Adicionar Alunos"
        "\n2 - Adicionar professores"
        "\n3 - Adicionar estágiários"
        "\n4 - Listar os dados"  
        "\n0 - Sair"
        "\nEscolha: "
    ))

    os.system("cls")

    if op == 1:
        adicionar_alunos()

    elif op == 2:
        adicionar_profssores()
           
    elif op == 3:
        adicionar_estagiarios()
        
    elif op == 4:
        opcao = int(input(
        "\n1 - Listar Alunos"
        "\n2 - Listar Professores"
        "\n3 - Listar estágiários"
        "\n4 - Listar todos dados"  
        "\n0 - Sair"
        "\nEscolha: "
        ))

        if opcao == 1 :
            listar_alunos(lista_de_alunos)
        elif opcao == 2:
            listar_professores(lista_de_professores)
        elif opcao == 3:
            listar_estagiarios(lista_de_estagiarios)
        elif opcao == 4:
            listar_alunos(lista_de_alunos)
            listar_professores(lista_de_professores)
            listar_estagiarios(lista_de_estagiarios)
        elif opcao == 0 :
            break
        else:
            print('opção inválida')

    elif op == 0:
        break

    else:
        print("Opção inválida.")