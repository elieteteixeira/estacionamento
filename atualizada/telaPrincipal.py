
import PySimpleGUI as sg
from telaRegistro import Registro




class TelaPrincipal():
    def __init__(self) -> None:
        self.entrada = Registro()

    def principal(self):

        menu = [
            ['&Registro', ['&Entrada', 'Saida']],
        ]

        layout = [
            [sg.Menu(menu, tearoff=False, pad=(200,1), background_color="#fff")],
        ]

        self.janela = sg.Window("Tela Principal", size=(960, 540), layout=layout, finalize=True)
        self.janela.set_min_size((960,540))

        return self.janela

tela = TelaPrincipal()
entrada = Registro()




janelaPrincipal, janelaEntrada = tela.principal(), None

while True:
    
    window, event, values = sg.read_all_windows()

    if window == janelaPrincipal and event == sg.WIN_CLOSED:
        break
    

    elif window == janelaPrincipal and event == "Entrada":
        janelaEntrada = entrada.tela()