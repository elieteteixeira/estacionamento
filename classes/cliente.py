
class cliente:

    def __init__(self, nome, cpf, endereco, telefone):

        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__telefone = telefone

    def __str__(self) -> str:
        return f'Nome: {self.__nome} cpf: {self.__cpf} endereco: {self.__endereco} telefone: {self.__telefone}'


         
    

    