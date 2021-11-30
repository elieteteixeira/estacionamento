import sqlite3

conexão = sqlite3.connect("banco_oficina.db")
cursor = conexão.cursor()

#### sentença sql para criar tabela

sql = ' CREATE TABLE funcionario('\
        'id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,'\
        'nome varchar(50),'\
        'cpf varchar(20),'\
        'contato varchar(20),'\
        'funcao varchar(30))'
cursor.execute(sql)

### setença para inserir registros na tabela

sql = 'insert into funcionario (nome, cpf, contato, funcao) values (?,?,?,?)'
registros = [('gusta', '123.345.567-34', '(86) 3212-5656', 'mecanico'), ('beatriz', '234.567.766-11', '(86) 98856-1111', 'recepcionista')]

for reg in registros:
    cursor.execute(sql, reg)

#### gravação no banco de dados sem commit os dados não são grvados

conexão.commit()

cursor.close()
conexão.close()