import sqlite3                                                                   ########importa sqlite

from sqlite3 import Error                                        ############ tratar de possiveis erros

conexao = sqlite3.connect('banco_oficina.db')           ############# cria o banco de dados e conexao caminho

##conexão com o banco de dados


cursor = conexao.cursor()                               ########### medoto que de tabelas criar alterar

                                  #  ##  ### ####  ######## variavel tabel e sequencia de criar tabelas

def criarTabela():

    try:
        cursor = conexao.cursor()
        cursor.execute(tabel)
        print('tabela criada com sucesso')

    except Error as ex:
        print(ex)

tabel = 'CREATE TABLE FUNCIONARIO('\
        'ID_pessoa integer primary key autoincrement,'\
        'nome varchar(50),'\
        'cpf varchar(15),'\
        'telefone varchar(15),'\
        'matricula integer(10),'\
        'função varchar(20))'

criarTabela()

tabel = tabel = 'CREATE TABLE CLIENTE('\
        'ID_pessoa integer primary key autoincrement,'\
        'nome varchar(40),'\
        'cpf varchar(15),'\
        'endereço varchar(35),'\
        'contato varchar(15),'\
        'veiculos varchar(50))'

criarTabela()

tabel = 'CREATE TABLE VEICULO('\
        'ID_pessoa integer primary key autoincrement,'\
        'modelo varchar(20),'\
        'placa varchar(10),'\
        'cor varchar(20),'\
        'proprietario varchar(40),'\
        'estacionados varchar(10))'

criarTabela()

tabel = 'CREATE TABLE PATIO('\
        'ID_pessoa integer primary key autoincrement,'\
        'descrição_vaga varchar(20),'\
        'taxa_hora varchar(10),'\
        'vagas integer(4))'

criarTabela()

tabel = 'CREATE TABLE ESTACIONAMENTO('\
        'ID_pessoa integer primary key autoincrement,'\
        'hora_entrada varchar(8),'\
        'hora_saida varchar(8),'\
        'valor_pago varchar(10),'\
        'veiculo varchar(20),'\
        'vaga integer(4))'

criarTabela()

tabel = 'CREATE TABLE STATUS_VAGA('\
        'ID_pessoa integer primary key autoincrement,'\
        'disponivel varchar(11),'\
        'indisponivel varchar(11))'

criarTabela()


conexao.commit
cursor.close()
conexao.close()