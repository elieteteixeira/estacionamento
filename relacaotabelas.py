import sqlite3
import os
from sqlite3.dbapi2 import Cursor, Error

def criarBanco():
    global conexao, Cursor
    if not os.path.exists('estacionamento.db'):
        conexao = sqlite3.connect('estacionamento.db')
        Cursor = conexao.cursor()

        sql_cliente =   'create table cliente('\
                        'id integer primary key autoincrement,'\
                        'nome varchar(50),'\
                        'cpf varchar(20),'\
                        'endereco varchar(40),'\
                        'contato varchar(15))' 

        sql_veiculo =   'create table veiculo('\
                        'id_veiculo integer primary key autoincrement,'\
                        'modelo varchar(20),'\
                        'placa varchar(10),'\
                        'cor varchar(20),'\
                        'proprietario varchar(40),'\
                        'id_cliente integer not null,'\
                        'FOREING KEY (id_cliente) REFERENCES cliente(id))'

        Cursor.execute(sql_cliente)
        Cursor.execute(sql_veiculo)
        conexao.commit()

def adicionar_cliente(nome): # parametro
    global conexao, Cursor
    sql_cliente = 'insert into contato(nome, cpf, endereco, contato) values(?,?,?,?)'
    Cursor.execute(sql_cliente, [nome ]) #passamos o comando sql e logo seguindo do parametro em forma de lista

def adicionar_veiculo(id_cliente, veiculos): #id_contato chave estrageira na tabela telefones fones?
    global conexao, Cursor
    sql_veiculo = 'insert into veiculos(modelo, placa, cor, proprietario id_cliente) values(?,?,?)' #id_contato foreid key
    for i in veiculos:
        Cursor.execute(sql_veiculo, [i[0], i[1], id_cliente])

def adicionar_veiculos():
    veiculos = []
    while True:
        modelo = input(f'modelo do carro: ')
        placa = input(f'numero da placa : ')
        cor = input(f'cor do veiculo : ')
        if modelo  == "":
            modelo = None
        if placa == "":
            placa = None
        if cor == "":
            cor = None

        veiculos.append((modelo, placa, cor))
        print(veiculos)
        conf = input('deseja cadastrar outro veiculo para esse cliente? (S/N)')
        if conf in 'Ss':
            pass
        if conf in 'Nn':
            break
    return veiculos

def cadastro():
    global conexao, Cursor
    if conexao == None:
        conexao = sqlite3.connect('estacionamento.db')
        Cursor = conexao.cursor()
    nome = input('entre com o nome do cliente : ')
    if nome == '':
        nome = None
    else:
        res = consultar('cliente', 'id,nome','nome', nome)
        print(res)
        if len(res)>0:
            id = res[0][0]
            res = consultar('veiculos', 'modelo, placa', 'id_cliente', id)
            if len(res)>0:
                print('veiculos cadastrados')
                for i in res:
                    print(i)
            else:
                print('não ha veiculos cadastrados para esse cliente!')
        else:
            fones = adicionar_veiculos()             
                ## sequencia sql parar adicionar registros
            try:
                adicionar_cliente(nome)
                id_cliente = Cursor.lastrowid
                adicionar_veiculos(id_cliente)
                conexao.commit()
            except:
                    print('erro de integridade do banco de dados!')

def atualizar_cliente():
    global conexao, Cursor
    if conexao == None:
        conexao = sqlite3.connect('estacionamento.db')
        Cursor = conexao.cursor()
    print('---------------------------------------------------------------')
    print('consultar/atualizar cliente')
    print('---------------------------------------------------------------')
    nome = input('digite o nome do cliente : ')
    sql = f"select * from cliente where nome like '%{nome}%'"## like busca aproximada
    Cursor.execute(sql)
    res = Cursor.fetchall()
    if len(res)>0:
        for i in res:
            print(i)
        resp = int(input('digite o nome do cliente a ser atualizado ou 0 para sair : '))
        if resp != 0:
            id_cliente = resp
            res = consultar('cliente', 'id,cliente', 'id', id_cliente)
            if len(res)>0:
                id_cliente = res[0][0]
                print(f'nomes : {res[0][1]}')
                res2 = consultar('veiculos', 'id_veiculo, modelo,placa', 'id_cliente', id_cliente)
                if len(res2)>0:
                    print('---------------------------------------------')
                    print('                  telefones                  ')
                    print('---------------------------------------------')
                    for i in res2:
                        print(i)
                    menu ('menu',['1-alterar cliente', '2-excluir cliente', '3-incluir veiculo', '4-alterar veiculo', '5-excluir veiculo', '6-sair']) ## tratar opção 2              
                    opc = int(input('entre com uma opção : '))
                    if opc == 1:
                        novo_cliente = input('digite o novo cliente : ')
                        sql = "UPTADE cliente SET nome = ? where id = ?"
                        Cursor.execute(sql, [novo_cliente, id_cliente])
                    elif opc == 2:
                        sql = "DELETE FROM cliente WHERE id = ? "
                        Cursor.execute(sql, [id_cliente])
                    elif opc == 3:
                        veiculos = adicionar_cliente()
                        adicionar_veiculos(id_cliente, veiculos )
                    elif opc == 4:
                        id_veiculo = int(input('digite o id do veiculo a ser alterado : '))
                        novo_modelo = input('digite o novo numero : ')
                        nova_placa = input('digite a nova descrição : ')
                        sql = "UPDATE telefones SET numero = ?, descricao = ? WHERE id_fone = ?"
                        Cursor.execute(sql, [novo_modelo, nova_placa, id_veiculo])
                    elif opc == 5:
                        id_veiculo = int(input('digite o id do telefone a ser excluido : '))
                        sql = "DELETE from telefones WHERE id_fone = ?"
                        Cursor.execute(sql, [id_veiculo])
                    elif opc == 6:
                        exit
                else:
                    print('sem veiculos cadastrados!')
                    resp = input('deseja incluir um novo veiculo? (S/N)')
                    if resp in 'Ss':
                        veiculos = adicionar_veiculos()
                        adicionar_cliente(id_cliente, veiculos)               
                conexao.commit()
            else:
                print('cliente não cadastrado!')
    else:
        print('cliente não cadastrado!')

def consultar(tabela, campos, campo_cond, valor):
    sql = f'select {campos} from {tabela} where {campo_cond} = ?'
    Cursor = conexao.cursor()
    Cursor.execute(sql, [valor])
    res = Cursor.fetchall()
    return res

def menu(cliente, veiculos):
    print(cliente)
    for i in veiculos:
        print(i)

def main():
    global conexao, Cursor
    conexao = None
    Cursor = None
    criarBanco()
    while True:
        menu ('menu_principal', ['1 - novo cliente', '2 - atualizar_cliente', '3 - sair'])
        opc = int(input('escolha uma opção : '))
        if opc == 1:
            cadastro()
        elif opc == 2:
            atualizar_cliente()
        elif opc == 3:
            break
    if Cursor != None:
        Cursor.close()
    if conexao != None:
        conexao.close()
main()