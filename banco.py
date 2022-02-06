from dbm.dumb import _Database
from email.policy import default
import peewee
from datetime import datetime

banco = peewee.SqliteDatabase('estacionamento.db')

class BaseModel(peewee.Model):
    
    class Meta:
        database = banco
        
class Veiculo(BaseModel):
    nome_cliente = peewee.CharField()
    tipo_veiculo = peewee.CharField()
    modelo_veiculo = peewee.CharField()
    cor_veiculo = peewee.CharField()
    placa_veiculo = peewee.CharField()
    
class Patio(BaseModel):
    hora_entrada = peewee.DateTimeField(default = datetime.now)
    hora_saida = peewee.DateTimeField()
    taxa = peewee.FloatField(1.00)
    valor_pagar = (hora_entrada - hora_saida) * taxa
    vaga = peewee.ForeignKeyField(Veiculo, backref='vagas')
    

banco.create_tables([Veiculo, Patio])
        
        
    