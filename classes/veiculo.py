
from Cliente import *;
from Estacionamento import *;

class Veiculo:

    def __init__(self, modelo, placa, cor, proprietario):
        self.__modelo = modelo
        self.__placa = placa
        self.__cor = cor
        if type(proprietario == Cliente):
            self.__proprietario = proprietario
        self.__estacionados = []

    @property
    def modelo(self):
        return self.__modelo
    @property
    def placa(self):
        return self.__placa
    @property
    def cor(self):
        return self.__cor
    @property
    def proprietario(self):
        return self.__proprietario


    def __str__(self):
          return f'Descrição: {self.__modelo}\nPlaca: {self.__placa}\ncor :{self.__cor}\n proprietario : {self.__proprietario}'




   
