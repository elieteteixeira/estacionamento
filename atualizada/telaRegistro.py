
import PySimpleGUI as sg
from crudBanco import *


class Registro:
    def __init__(self) -> None:
        pass

    def tela(self):
        tipo = listaTipos()
        lista_tipos = []
        for i in tipo:
            lista_tipos.append(i.descricao)
        
        layout = [
            [sg.Text("Cliente"), sg.Input(key="-CLIENTE-")],            
            [sg.Text("Placa"), sg.Input(key="-PLACA-")],
            [sg.Text("Tipo Veiculo")],

            [sg.Listbox(values=lista_tipos, size=(50, 2), key='-LIST-TIPO-', enable_events=True)],
            [sg.Button("Salvar")]


        ]
        self.janela = sg.Window("Tela Principal", size=(960, 540), layout=layout, finalize=True)
        self.janela.set_min_size((960,540))

        while True:
            event, values = self.janela.Read()
            if event == sg.WINDOW_CLOSED or event == "Sair":
                break




        return self.janela
