
class cliente:

    def __init__(self, nome, cpf, endereco, contato):

        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__contato = contato
        self.__veiculos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def contato(self):
        return self.__contato

    def cadastrarVeiculo(self, veiculo):
        self.__veiculos.append(veiculo)
        print('o veiculo  modelo {}, foi cadastrado em nome do cliente {}'.format(veiculo.descricao, self.__nome))


    def __str__(self):
        cl = 'cliente :\n'
        s1 = (' nome :{}\ncpf :{}\ncontato :{}\n'.format(self.__nome,self.__cpf,self.__contato))
        s2 = 'relação dos veiculos de {}'.format(self.__nome)+'\n'
        s3 = " "
        for i in range(len(self.__veiculos)):
            s3 = s3+'veiculo :'+self.__veiculos[i].descricao+ ' ' +'placa :'+self.__veiculos[i].placa+'\n'
        return cl+s1+s2+s3


         
    

    