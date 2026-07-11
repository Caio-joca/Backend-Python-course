'''
Neste tipo de arquivo vamos botar as funções que vamos puxar no main, é um arquivo apenas com funções.
'''

import sqlite3
from pathlib import Path


pasta_atual = Path(__file__).parent
caminho_banco = pasta_atual / "biblioteca.db"


# Conexão com o banco por meio de Python
def conectar():
    conexao = sqlite3.connect(caminho_banco)
    return conexao


# Criação da tabela que precisa de título, autor, gênero, número de páginas e resumo
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS biblioteca(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        genero TEXT NOT NULL,
        paginas INTEGER NOT NULL,
        resumo TEXT NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()


# Função para inserir livros
def inserir_livros(titulo, autor, genero, paginas, resumo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO biblioteca(titulo, autor, genero, paginas, resumo)
    VALUES(?, ?, ?, ?, ?)
    """, (titulo, autor, genero, paginas, resumo))

    conexao.commit()
    conexao.close()


# Função para buscar livros
def BuscarLivros():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM biblioteca")
    biblioteca = cursor.fetchall()

    conexao.close()

    return biblioteca


# Função para buscar um livro específico pelo ID
def BuscarLivroPorId(id_livro):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM biblioteca
    WHERE id = ?
    """, (id_livro,))

    livro = cursor.fetchone()

    conexao.close()

    return livro


# Função para alterar livros
def alterar_livro(id_livro, titulo, autor, genero, paginas, resumo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE biblioteca
    SET titulo = ?, autor = ?, genero = ?, paginas = ?, resumo = ?
    WHERE id = ?
    """, (titulo, autor, genero, paginas, resumo, id_livro))

    conexao.commit()
    conexao.close()


# Função para excluir livros
def excluir_livro(id_livro):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM biblioteca
    WHERE id = ?
    """, (id_livro,))

    conexao.commit()
    conexao.close()