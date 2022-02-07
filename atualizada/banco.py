
from asyncio.windows_events import NULL
from email.policy import default
from peewee import *
import datetime

banco = SqliteDatabase('estacionamento.db', pragmas={'foreign_keys': 1})

class BaseModel(Model):
    
    class Meta:
        database = banco

class Cliente(BaseModel):
    nome = CharField()



class TipoVeiculo(BaseModel):
    descricao = CharField()
    preco = FloatField()
       
# class Veiculo(BaseModel):
#     placa_veiculo = CharField()
#     nome_cliente = ForeignKeyField(Cliente, backref='clientes')
#     tipo_veiculo = ForeignKeyField(TipoVeiculo, backref="tipos")
#     modelo_veiculo = CharField()
#     cor_veiculo = CharField()
    

class RegistroEntradaSaida(BaseModel):
    placa = CharField()
    cliente = ForeignKeyField(Cliente, backref='registros')
    tipoVeiculo = ForeignKeyField(TipoVeiculo, backref='registros')
    entrada = DateTimeField(default=datetime.datetime.now)
    saida = DateField(default=NULL)
    valor_pagar = FloatField(default=0.0)

class Patio(BaseModel):
    descricao = CharField()
    quantidade_vagas = IntegerField()
    

banco.create_tables([Cliente, TipoVeiculo, Patio, RegistroEntradaSaida])
        
        
    