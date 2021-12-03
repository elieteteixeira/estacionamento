

class Patio:
    def __init__(self, descricao, taxaHora):
        self.__descricao = descricao
        self.__taxaHora = taxaHora
        self.__vagas = []

    @property
    def taxaHora(self):
        return self.__taxaHora