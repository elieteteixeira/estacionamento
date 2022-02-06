from peewee import *
import peewee
import datetime
 
banco = peewee.SqliteDatabase('estaciona.db')

class BaseModel(peewee.Model):
    
    class Meta:
        
        database = banco
        
class Usuario(BaseModel):
    
    login = peewee.CharField()
    senha = peewee.CharField()
    nome = peewee.CharField()
    
class Cliente(BaseModel):
    nome_cliente = peewee.CharField()
    cpf_cliente = peewee.CharField()
    telefone_cliente = peewee.CharField()
    veiculos = peewee.CharField() #lista
    
class Veiculo(BaseModel):
    modelo_veiculo = peewee.CharField()
    cor_veiculo = peewee.CharField()
    placa_veiculo = peewee.CharField()
    nome_proprietario = peewee.CharField()
    #Estacionamento = uma lista de Estacionamento
    id_proprietario = peewee.ForeignKeyField(Cliente)
    
class Estacionamento(BaseModel):
    entrada = peewee.DateField()
    saida = peewee.DateField()
    valor_pago = peewee.FloatField()
    vaga = peewee.CharField()
    veiculo = peewee.CharField()
    id_veiculo = peewee.ForeignKeyField(Veiculo)
    id_vaga = peewee.ForeignKeyField(vaga)
    
class Patio(BaseModel):
    descricao = peewee.CharField()
    taxa_hora = peewee.FloatField()
    vagas = peewee.CharField
    
class Vaga(BaseModel):
    numero_vaga = peewee.IntegerField()
    patio = peewee.CharField()
    status = peewee.CharField()
    #Estacionamento = lista
    
class StatusVaga(BaseModel):
    disponivel = peewee.CharField()
    indisponivel = peewee.CharField()
     
    
if __name__ == '__main__' :
    try:
        Usuario.create_table()
        print("tabela criada!!!")
    except peewee.OperationalError :
        print("tabela ja existe!!!")
        
    try:
        Cliente.create_table()
        print("tabela criada!!!")
    except peewee.OperationalError :
        print("tabela ja existe!!!")
        
    try:
        Veiculo.create_table()
        print("tabela criada!!!")
    except peewee.OperationalError:
        print("tabela ja exite!!!")
        
    try:
        StatusVaga.create_table()
        print("tabela criada!!!")
    except peewee.OperationalError:
        print("tabela ja exite!!!")
        
    try:
        Estacionamento.create_table()
        print("tabela criada!!!")
    except peewee.OperationalError:
        print("tabela ja exite!!!")
        
    try:
        Vaga.create_table()
        print("tabela criada!!!")
    except peewee.OperationalError:
        print("tabela ja exite!!!")
        
    try:
        Patio.create_table()
        print("tabela criada!!!")
    except peewee.OperationalError:
        print("tabela ja exite!!!")