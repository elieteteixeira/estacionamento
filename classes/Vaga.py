from StatusVaga import *;

class Vaga:
    def __init__(self, numeroVaga, patio, status, estacionar, ultimoEstacionar):
        self.__numeroVaga = numeroVaga
        self.__patio = patio
        if type(status == StatusVaga):
            self.__status = status

    @property
    def numeroVaga(self):
        return self.__numeroVaga

    @property
    def status(self):
        return self.__status