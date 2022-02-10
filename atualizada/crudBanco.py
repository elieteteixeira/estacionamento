
from xmlrpc.client import Error
from atualizada.banco import TipoVeiculo
from banco import *


# Metodos
sucesso = "Salvo com sucesso! "
error = "Erro ao salvar registro"


def cadastratarTipoVeiculo(descricao, preco):
    try:
        TipoVeiculo.create(
            descricao=descricao,
            preco=preco
        )

        print(sucesso)

    except Error as e:
        print(e)


def listaTipos():
    query = TipoVeiculo.select()
    return query


def getTipoId(id):
    tipo = TipoVeiculo.get(TipoVeiculo.id == id)
    return tipo


def atualizarTipo(id, descricao, preco):
    query = (TipoVeiculo.update(descricao=descricao,
             preco=preco).where(TipoVeiculo.id == id))
    query.execute()


def deleteTipo(id):
    TipoVeiculo.delete().where(TipoVeiculo.id == id).execute()
    print('Deletado com sucesso')


# Cliente
def cadastratarCliente(nome):
    try:
        Cliente.create(
            nome=nome
        )

        print(sucesso)

    except Error as e:
        print(e)


def listaClientes():
    query = Cliente.select()
    return query


def getClienteId(id):
    cliente = Cliente.get(Cliente.id == id)
    return cliente


def atualizarCliente(id, nome):
    query = (Cliente.update(nome=nome).where(Cliente.id == id))
    query.execute()


def deleteTipo(id):
    Cliente.delete().where(Cliente.id == id).execute()
    print('Deletado com sucesso')


# Patio
def cadastratarPatio(descricao, quantidade):
    try:
        Patio.create(
            descricao=descricao,
            quantidade_vagas=quantidade
        )

        print(sucesso)

    except Error as e:
        print(e)


def listaPatio():
    query = Patio.select()
    return query


def getPatioId(id):
    patio = Patio.get(Patio.id == id)
    return patio


def atualizarPatio(id, nome):
    query = (Patio.update(nome=nome).where(Patio.id == id))
    query.execute()


def deletePatio(id):
    Patio.delete().where(Patio.id == id).execute()
    print('Deletado com sucesso')


# Registro de Entrada


def cadastrarEntrada(placa, cli_id, tipo_id):
    cliente = Cliente.get(Cliente.id == cli_id)
    tipo = TipoVeiculo.get(TipoVeiculo.id == tipo_id)
    RegistroEntradaSaida.create(
        placa=placa,
        cliente_id=cliente,
        tipoVeiculo_id=tipo
    )

    patio = Patio.get()
    vaga = patio.quantidade_vagas - 1
    patio.quantidade_vagas = vaga
    patio.save()

# def cadastrarSaida(placa, cli_id, tipo_id):
#     cliente = Cliente.get(Cliente.id == cli_id)
#     tipo = TipoVeiculo.get(TipoVeiculo.id == tipo_id)
#     RegistroEntradaSaida.create(
#     placa = placa,
#     cliente_id = cliente,
#     tipoVeiculo_id = tipo
#     )

#     patio = Patio.get()
#     vaga = patio.quantidade_vagas + 1
#     patio.quantidade_vagas = vaga
#     patio.save()


def listaPatio():
    query = Patio.select()
    return query


def getPatioId(id):
    patio = Patio.get(Patio.id == id)
    return patio


def atualizarPatio(id, nome):
    query = (Patio.update(nome=nome).where(Patio.id == id))
    query.execute()


def deletePatio(id):
    Patio.delete().where(Patio.id == id).execute()
    print('Deletado com sucesso')


# def tipoGetId(id):
#     TipoVeiculo.
# def cadastrar_veiculo():
#     try:
#         nome_cli = input('entre com o nome do cliente : ')
#         tipo_veic = input('tipo do veiculo : ')
#         modelo_veic = input("entre com o modelo do veiculo : ")
#         cor_veic = input('entre cor a cor do veiculo : ')
#         placa_veic = input('entre com a placa do veiculo : ')
#         Veiculo.create(nome_cliente = nome_cli, tipo_veiculo=tipo_veic, modelo_veiculo=modelo_veic, cor_veiculo=cor_veic, placa_veiculo=placa_veic)
#         print('entrada de veiculo inserida no sistema')
#     except peewee.OperationalError:
#         print('falha na operação!!!')

# def consultar_placa():
#     print('consultar veiculo por placa')
#     print('8 consultar veiculo.')
#     print('9 sair da cnsulta.')
#     opc = int(input('escolha 8 para consultar ou 9 para sair : '))
#     if(opc == 8):
#         placa = input('digite o numero da placa do veiculo : ')
#         res = Veiculo.select().where(Veiculo.placa_veiculo == placa).get()
#         print('-----------------------------------')
#         print('veiculo modelo {}\nproprietario {}'.format(res.modelo_veiculo, res.nome_cliente))
#         print('-----------------------------------')
#     elif(opc == 9):
#         Break
#     else:
#         print('veiculo não encontrado !!')


# def Menu():

#     while True:
#         print('1 CADASTRAR VEICULOS. ')
#         print('2 SAIDA DE VEICULOS. ')
#         print('3 CONSULTAR VEICULOS NO PATIO. ')
#         print('5 sair do sistema')
#         opc = int(input("escolha uma opção : "))

#         if(opc == 1):
#             cadastrar_veiculo()
#         elif(opc == 2):
#             pass
#         elif(opc == 3):
#             consultar_placa()
#         elif(opc == 5):
#             print("finalizando o sistema obg !!!")
#             break
# Menu()
 # Usar para criar registros de teste
# patio = cadastratarPatio("Principal", 20)
# cliente = cadastratarCliente("Desconhecido")

# cadastratarTipoVeiculo('Carro', 5.00)
# deleteTipo(2)
# atualizarTipo(2, "carroça", 50.00)
# valor = getTipoId(2)

# print(valor.descricao)

# cadastrarEntrada("NIX 999", 1, 1)
