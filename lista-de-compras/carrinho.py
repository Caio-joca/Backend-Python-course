class Carrinho:
    def __init__(self, lista):
        self.lista = lista

    def listar_produtos(self):
        if len(self.lista) == 0:
            print("Carrinho vazio.")
        else:
            for produto in self.lista:
                subtotal = produto.preco * produto.quantidade
                print(f"Nome: {produto.nome} | Preço: {produto.preco} | Quantidade: {produto.quantidade} | Subtotal: {subtotal}")

    def remover_produto(self, nome):
        if len(self.lista) == 0:
            print("Carrinho vazio.")
        else:
            encontrado = False

            for produto in self.lista:
                if produto.nome == nome:
                    self.lista.remove(produto)
                    encontrado = True
                    print("Produto removido.")
                    break

            if encontrado == False:
                print("Produto não encontrado.")

    def calcular_total(self):
        if len(self.lista) == 0:
            print("Carrinho vazio.")
        else:
            total = 0

            for produto in self.lista:
                total += produto.preco * produto.quantidade

            print(f"Total da compra: {total}")