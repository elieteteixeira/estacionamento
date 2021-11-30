import sqlite3
from sqlite3.dbapi2 import Cursor
conexão = sqlite3.connect('estacionamento.db')
Cursor = conexão.cursor()

#### sentença sql para criar tabela

sql = 'CREATE TABLE funcionario('\
        'ID_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,'\
        'nome varchar(50),'\
        'cpf varchar(20),'\
        'endereço varchar(50),'\
        'telefone varchar(25),'\
        'matricula integer(10))'

Cursor.execute(sql)

### setença para inserir registros na tabela

sql = 'insert into funcionario(nome, cpf, endereço, telefone, matricula) values (?,?,?,?,?)'
registros = [('alisson', '123.456.765-11', 'rua 13, parque alvorada, timon', '(86) 98822-1111', 1234567), ('valisson', '222.345.654-00', 'rua 03, parque piaui, timon', '(86) 98822-1333', 4455511)]

for reg in registros:
    Cursor.execute(sql, reg)

#### gravação no banco de dados sem commit os dados não são grvados

conexão.commit()

Cursor.close()
conexão.close()




