#Aqui vamos criar tuod relacionado a tabelas dos bancos de dados

import sqlite3
from pathlib import Path
PASTA_ATUAL = Path(__file__).parent
PASTA_DATABASE = PASTA_ATUAL / "banco"
PASTA_DATABASE.mkdir(exist_ok=True)

BANCO = PASTA_DATABASE / "biblioteca.db"

#Funçao para podermos nosconectar com o banco de dados, e nunca masi ficar escrvendo a mesma coisa
def conectar():
    return sqlite3.connect(BANCO)

#Função que vamos estar utilizando para poder criar as tabelas
def criar_tabelas():
    conn= conectar()
    cursor = conn.cursor()
    #Mandando para dentro do banco de dados esse comando
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        genero TEXT,
        paginas INTEGER,
        quantidade INTEGER
    )
    """)

    #Mandando comando agora para poder criar a tabela de usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT,
        telefone TEXT,
        email TEXT
    )
    """)
    
    #Cmando para os empréstimos agora
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emprestimos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        livro_id INTEGER,
        data_emprestimo TEXT,
        data_devolucao TEXT,
        status TEXT,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY(livro_id) REFERENCES livros(id)
    )
    """)

    #Comitando agora tudo que foi feito para a criação destas tabelas.
    conn.commit()
    conn.close()
    