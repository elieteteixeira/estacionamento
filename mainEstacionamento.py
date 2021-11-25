from classes.funcionario import funcionario
from classes.cliente import cliente
from classes.veiculo import veiculo

# funcionario( nome, cpf, endereco, telefone,matricula
# cliente (nome, cpf, endereco, contato
# veiculo ( descricao, placa, proprietario

Pedro = funcionario('Pedro João Gomes', '94066985410',
                    'Quadra JA casa 801 Pires', '2636524170', '02100')
Erinalda = cliente('Erinalda Maria Sousa', '84567945623',
                   'Rua SP, Nº 10 Servada', '(86) 5895-2631')
Joao = cliente('Joao', '12312312345',
               'Rua Ma N 100 Manganga', '(86) 8998-4646')
Honda = veiculo('Moto Honda Preta', 'CD 2021')
Gol = veiculo('Gol vermelho', 'mxd 2022')
Celta = veiculo('celta azul', 'mdr 2020')

print(Pedro)

print(Honda)
print(Gol)
print(Celta)

# Precisa implementar os métodos
# Erinalda.cadastrarVeiculo(Honda)
# Erinalda.cadastrarVeiculo(Gol)
# Joao.cadastrarVeiculo(Celta)
print(Erinalda)
print(Joao)
