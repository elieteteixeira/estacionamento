
class Patio:
    def __init__(self, descricaovaga, taxaHora):
        self.__descricaovaga = descricaovaga
        self.__taxaHora = taxaHora
        self.__vagas = []

    @property
    def taxaHora(self):
        return self.__taxaHora