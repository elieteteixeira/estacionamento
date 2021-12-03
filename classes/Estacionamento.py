from Veiculo import *;
from Vaga import *;

class Estacionamento:
    def __init__(self, horaEntrada, horaSaida, valorPago, veiculo, vaga):
        self.__horaEntrada = horaEntrada
        self.__horaSaida = horaSaida
        self.__valorPago = valorPago
        if type(veiculo == Veiculo):
            self.__veiculo = veiculo
        if type(vaga == Vaga):
            self.__vaga = vaga

    @property
    def horaEntrada(self):
        return self.__horaEntrada
    @property
    def horaSaida(self):
        return self.__horaSaida