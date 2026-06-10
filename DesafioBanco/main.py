'''Preciso fazer um programa que é um banco, primeiro preciso
criar uma classe Banco para receber todos os dados,
e realizar funções internas para processamento de dados
depois disso preciso criar um while para fazer um 
menu para o usuário, e funções para chamar o banco de maneiras
diferentes, como individuais, ou em grupo.

o número de conta deve ser aleatório e não deve se repetir
'''
# Para criação de número aleatório vou importar a biblioteca random
import random
import os
from Banco import BancoDinheiro

Lista_Contas = []
while True:
    decisao = 1
    print("\nCadastro de Banco")
    print("1 - Cadastrar Conta ")
    print("2 - Depositar ")
    print("3 - Sacar ")
    print("4 - Extrato de uma conta ")
    print("5 - Listar todas as contas ")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == '1':
        os.system('cls')
        while True :
            try :
                NomeConta = input("nome da conta: ")
                Saldo = float(input("Saldo a adicionar: "))
                Limite = float(input("limite para a conta: "))
                break
            except ValueError :
                print('voce digitou errado')
        while True:
            numero =  random.randint(1000,5000)
            for i in Lista_Contas :
                if numero == i.conta_num :
                    numero =  random.randint(1000,5000)
                elif numero != i:
                    break
            NumeroConta = numero
            break
        contas = BancoDinheiro(NomeConta, NumeroConta,Saldo, Limite)
        Lista_Contas.append(contas)
        print(f"Número da conta : {NumeroConta}")
        print("Conta cadastrada com sucesso.")
    elif opcao == '2' :
        os.system('cls')
        while True :
            try :
                NumeroConta = float(input("Qual num da conta: "))
                Saldo = float(input("Saldo a adicionar: "))
                for i in Lista_Contas :
                    if i.conta_num == NumeroConta  :
                        decisao = NumeroConta
                    else:
                        print('O número de conta digitado não existe')
                if decisao ==NumeroConta :
                    break  
            except ValueError :
                print('voce digitou errado')
        for i in Lista_Contas :
            if i.conta_num == NumeroConta :
                i.depositar(Saldo)
    elif opcao == '3' :
        os.system('cls')
        while True :
            try :
                NumeroConta = float(input("Qual num da conta: "))
                ValorSacar = float(input("Saldo a sacar: "))
                for i in Lista_Contas :
                    if i.conta_num == NumeroConta  :
                        decisao = NumeroConta
                    else:
                        print('O número de conta digitado não existe')
                if decisao ==NumeroConta :
                    break
            except ValueError :
                print('Voce escreveu errado')
        for i in Lista_Contas :
            if i.conta_num == NumeroConta :
                i.sacar(ValorSacar)
    elif opcao == '4' :
        os.system('cls')
        while True :
            try :
                NumeroConta = float(input("Qual num da conta: "))
                for i in Lista_Contas :
                    if i.conta_num == NumeroConta  :
                        decisao = NumeroConta
                    else:
                        print('O número de conta digitado não existe')
                if decisao ==NumeroConta :
                    break
            except ValueError :
                print('Voce digitou errado')
        for i in Lista_Contas :
            if i.conta_num == NumeroConta :
                i.mostrar_extrato()
    elif opcao == '5' :
        os.system('cls')
        print("Todas as contas: ")
        for i in Lista_Contas :
            print('------------------------------------------------------------------------------------------\n')
            print(f'Numero da conta : {i.conta_num} | nome da conta : {i.nome} | Saldo da conta {i.saldo}\n')
    elif opcao == '0' :
        break
    else :
        print('Escrita errada\n')