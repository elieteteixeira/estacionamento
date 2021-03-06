class Funcionario:
    def __init__(self, nome, cpf, endereco, telefone, matricula, funcao):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__telefone = telefone
        self.__matricula = matricula
        self.__funcao = funcao
        self.__funcionarios = []


    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def matricula(self):
        return self.__matricula

    @property
    def funcao(self):
        return self.__funcao

    def addFuncionario(self, funcionario):
        self.__funcionarios.append(funcionario)
        print('funcionario adicionado')

    def excluirFuncionario(self, funcionario):
        self.__funcionarios.remove(funcionario)
        print('funcionario excluido')


    def __str__(self) -> str:
        return f'Nome: {self.__nome}\nCPF: {self.__cpf}\nEndereco: {self.__endereco}\nTelefone: {self.__telefone}\nMatricula: {self.__matricula}\nFunção: {self.__funcao}'



