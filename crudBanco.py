from ast import Break
from select import select
from urllib.parse import parse_qs
from banco import *

def cadastrar_veiculo():
    try:
        nome_cli = input('entre com o nome do cliente : ')
        tipo_veic = input('tipo do veiculo : ')
        modelo_veic = input("entre com o modelo do veiculo : ")
        cor_veic = input('entre cor a cor do veiculo : ')
        placa_veic = input('entre com a placa do veiculo : ')
        Veiculo.create(nome_cliente = nome_cli, tipo_veiculo=tipo_veic, modelo_veiculo=modelo_veic, cor_veiculo=cor_veic, placa_veiculo=placa_veic)
        print('entrada de veiculo inserida no sistema')
    except peewee.OperationalError:
        print('falha na operação!!!')
      
def consultar_placa():
    print('consultar veiculo por placa')
    print('8 consultar veiculo.')
    print('9 sair da cnsulta.')
    opc = int(input('escolha 8 para consultar ou 9 para sair : '))
    if(opc == 8):
        placa = input('digite o numero da placa do veiculo : ')
        res = Veiculo.select().where(Veiculo.placa_veiculo == placa).get()
        print('-----------------------------------')
        print('veiculo modelo {}\nproprietario {}'.format(res.modelo_veiculo, res.nome_cliente))
        print('-----------------------------------')    
    elif(opc == 9):
        Break  
    else:    
        print('veiculo não encontrado !!')
        
        

     
def Menu():
    
    while True:
        print('1 CADASTRAR VEICULOS. ')
        print('2 SAIDA DE VEICULOS. ')
        print('3 CONSULTAR VEICULOS NO PATIO. ')
        print('5 sair do sistema')
        opc = int(input("escolha uma opção : "))
        
        if(opc == 1):
            cadastrar_veiculo()
        elif(opc == 2):
            pass
        elif(opc == 3):
            consultar_placa() 
        elif(opc == 5):
            print("finalizando o sistema obg !!!")
            break
        
        
Menu()