import sqlite3
from pathlib import Path


pasta_atual = Path(__file__).parent
caminho_banco = pasta_atual / "veiculos.db"


def conectar():
    conexao = sqlite3.connect(caminho_banco)
    return conexao


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS veiculos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        placa TEXT NOT NULL,
        proprietario TEXT NOT NULL,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()


def inserir_veiculo(placa, proprietario, marca, modelo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO veiculos(placa, proprietario, marca, modelo)
    VALUES(?, ?, ?, ?)
    """, (placa, proprietario, marca, modelo))

    conexao.commit()
    conexao.close()


def buscar_veiculos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM veiculos")
    veiculos = cursor.fetchall()

    conexao.close()

    return veiculos