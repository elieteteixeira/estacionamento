import sqlite3
from sqlite3.dbapi2 import Cursor, Error
conexão = sqlite3.connect('estacionamento.db')
Cursor = conexão.cursor()

#### inserir registros na tabela

varsql = ""

def inserir(conexão, sql):
    try:
        Cursor.execute(varsql)
        conexão.commit()
        print("registros inseridos")

    except Error as ex:
        print(ex)


def deletar(conexão, sql):
    try:
        Cursor.execute(varsql)
        conexão.commit()
        print("registros excluidos")

    except Error as ex:
        print(ex)

## para inserir 
inserir(conexão, varsql)

## para excluir

deletar(conexão, varsql)