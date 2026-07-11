import os
from product import Produto
from carrinho import Carrinho


objectlist = []


def adicionar_produto():
    quantidade_produtos = int(input("Quantos produtos você quer adicionar? "))

    for quant in range(quantidade_produtos):
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade do produto: "))

        produto_object = Produto(nome, preco, quantidade)
        objectlist.append(produto_object)

        print("Produto adicionado ao carrinho.")


def listar_carrinho():
    carrinho_object = Carrinho(objectlist)
    carrinho_object.listar_produtos()


def remover_produto():
    carrinho_object = Carrinho(objectlist)
    nome = input("Digite o nome do produto que deseja remover: ")
    carrinho_object.remover_produto(nome)


def calcular_total():
    carrinho_object = Carrinho(objectlist)
    carrinho_object.calcular_total()


while True:
    op = int(input(
        "\n1 - Adicionar produto"
        "\n2 - Remover produto"
        "\n3 - Listar carrinho"
        "\n4 - Calcular total"
        "\n0 - Sair"
        "\nEscolha: "
    ))

    os.system("cls")

    if op == 1:
        adicionar_produto()

    elif op == 2:
        remover_produto()

    elif op == 3:
        listar_carrinho()

    elif op == 4:
        calcular_total()

    elif op == 0:
        break

    else:
        print("Opção inválida.")