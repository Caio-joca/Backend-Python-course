'''

Aqui vou copiar o que o sor passou no quadro para copiar.

isso é para o banco de dados sqlite
'''

#Priemiramente importamos a biblioteca do próprio pytohn para banco de dados
import sqlite3

#é o canal de comunicação com o banco de dados.
conexao = sqlite3.connect("empresa.db")

#cursor é quem vai mandar no canal de conexão com o sqlite3
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
    )
""")

print("Tabela criada com sucesso !")

conexao.commit()
conexao.close()


#Depois disso temos a incersçao de dados dentro desta tabela

nome = "Monitor"
preco = 899.90

#Sempre temos que fazer uma conexão com o banco de daddos
conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

cursor.execute("""
INSERT INTO produtos(nome, preco)
VALUES(?, ?)
""", (nome, preco))

conexao.commit()

print("Produto Cadastrado")

conexao.close()
conexao.close

#Agora vamos pegar dados de dentro do banco ded ados e passar para a memória RAM da cpu para poder utilizar eles.
conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM produtos")

produtos = cursor.fetchall()

for produto in produtos :
    print(produto)

conexao.close()

#Vamos atualizar agora alguns itens de dentro do banco de dados.
conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()


#Aqui nós pegamos a variável x, o que nós queremos trocar e depois com o id nós botamos a variável y para trocar especificamente onde queremos trocar
cursor.execute("""
UPDATE produtos
SET preco = ?
WHERE id = ?   
""", (1200, 1))

conexao.commit()

print("produto atualizado")

conexao.close()

#Agora vamos fazer o DELETE de itens de dentro de um banco SQL.

conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

cursor.execute("""
DELETE FROM produtos
WHERE id=?
""", (1,))

conexao.commit()

print("Produto removido!")

conexao.close()

#Aqui criei o banco de dados em um local específico da pasta de arquivos, e sempre que suisermos entrar dentro destes arquivos em específico temos que botar o caminho dele completo, mas também podemos abrir um banco de dadso e fechar ele somente no final do código.
conexao = sqlite3.connect("C:/Users/Curso/Desktop/Auladia25do4/BackEnd/Aula 19/BancodeDados/loja.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

conexao.commit()
while True:
    print("\n=== SISTEMA DE PRODUTOS ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))

        cursor.execute("""
        INSERT INTO produtos(nome, preco)
        VALUES(?, ?)
        """, (nome, preco))

        conexao.commit()

        print("Produto cadastrado!")


        """Aqui nós vamos ler uma informação de dentro do vanco de dados, fazemos isso com o comando SELECT * FROM, onde com o asterísco conseguimos selecionar todas as coluas de dentro de um banco de dados, todas as variáveis específicas que estão sendo gaurdadads dentro desse Banco, todos os X dessa matriz. Como se fizessemos isso : SELECT id, nome, preco FROM produtos;

        E esses dados vão ser pegos de toda a tabela, de todos os ID's ou seja linhas, pois não tem nenhuma condição dizendo para não pegar de todas as linhas, caso na próxima linha esteja escrita WHERE id = 1;
        Aí sim nós estariamos dando uma ordem específica de qual linha nós queremos que ele pegue o dados.

        Depois de pegar todos os itens e guardar dentro e uma variavel nós temos que fazer uso do comado fetchall, ele pega todos os valores do banco de dadso, que eram de variáveis de memória flash e bota em variáveis de memória RAM do python.
                            ⬇️   
        """
    elif opcao == "2":
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        print("\nLISTA DE PRODUTOS")

        for produto in produtos:
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R$ {produto[2]:.2f}")

    elif opcao == "3":
        id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
        novo_nome = input("Novo nome do produto: ")
        novo_preco = float(input("Novo preço: "))

        cursor.execute("""
        UPDATE produtos
        SET nome = ?, preco = ?
        WHERE id = ?
        """, (novo_nome, novo_preco, id_produto))

        conexao.commit()

        print("Produto atualizado!")

    elif opcao == "4":
        id_produto = int(input("Digite o ID do produto que deseja excluir: "))

        cursor.execute("""
        DELETE FROM produtos
        WHERE id = ?
        """, (id_produto,))

        conexao.commit()

        print("Produto excluído!")

    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")

conexao.close()