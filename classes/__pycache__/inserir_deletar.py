import sqlite3
from sqlite3.dbapi2 import Cursor, Error
conexão = sqlite3.connect('estacionamento.db')
Cursor = conexão.cursor()

#### inserir registros na tabela

varsql = ""
## função de inserir registros na tabela
def inserir(conexão, sql):
    try:
        Cursor.execute(varsql)
        conexão.commit()
        print("registros inseridos")

    except Error as ex:
        print(ex)

## função de deletar registros na tabela
def deletar(conexão, sql):
    try:
        Cursor.execute(varsql)
        conexão.commit()
        print("registros excluidos")

    except Error as ex:
        print(ex)

## função de atualização dos dados das tabelas
def atualizar(conexão, sql):
    try:
        Cursor.execute(varsql)
        conexão.commit()
        print("registros atualizados")

    except Error as ex:
        print(ex)

## função de consulta no banco de dados
def consultar(conexão, sql):    
    Cursor.execute(varsql)
    resultado = Cursor.fetchall()
    return resultado
