
class funcionario:
    def __init__(self, nome, cpf, endereco, telefone,matricula):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__telefone = telefone
        self.__matricula = matricula

    def __str__(self) -> str:
        return f'Nome: {self.__nome} CPF: {self.__cpf} Endereco: {self.__endereco} Telefone: {self.__telefone} Matricula: {self.__matricula}'
