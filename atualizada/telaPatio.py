
import PySimpleGUI as sg
from crudBanco import *
from banco import Patio


class TelaPatio:
    def __init__(self) -> None:
        pass

    def tela(self):       
        layout = [
            [sg.Text("Descricao"),sg.Input(key="-DESCRICAO-", do_not_clear=False)],
            [sg.Text("Quant. Vagas"),sg.Input(key="-VAGAS-", do_not_clear=False)],              
            [sg.Button("Salvar", key='-SALVAR-')]           
         


        ]
        self.janela = sg.Window("Tipo Veiculo", size=(450, 150), layout=layout, finalize=True)
        # self.janela.set_min_size((450,450))

        while True:
            event, values = self.janela.Read()
            if event == sg.WINDOW_CLOSED or event == "Sair":
                break

            if event == '-SALVAR-':
                descricao = values['-DESCRICAO-']
                quantidade = values['-VAGAS-']
                cadastratarPatio(descricao, quantidade)
                [sg.popup('Cadastrado com sucesso !', text_color="#04BEB3")]



        return self.janela
