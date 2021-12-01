class Vaga:
    def __init__(self, numeroVaga, status):
        self.__numeroVaga = numeroVaga
        self.__status = status

    @property
    def numeroVaga(self):
        return self.__numeroVaga

    @property
    def status(self):
        return self.__status