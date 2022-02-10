
import PySimpleGUI as sg
from crudBanco import *
from banco import TipoVeiculo as tipo


class TelaTipoVeiculo:
    def __init__(self) -> None:
        pass

    def tela(self):       
        layout = [
            [sg.Text("Tipo Veiculo"),sg.Input(key="-TIPO-", do_not_clear=False)],
            [sg.Text("Preco"),sg.Input(key="-PRECO-", do_not_clear=False)],              
            [sg.Button("Salvar", key='-SALVAR-')]           
         


        ]
        self.janela = sg.Window("Tipo Veiculo", size=(450, 150), layout=layout, finalize=True)
        # self.janela.set_min_size((450,450))

        while True:
            event, values = self.janela.Read()
            if event == sg.WINDOW_CLOSED or event == "Sair":
                break

            if event == '-SALVAR-':
                tipo = values['-TIPO-']
                preco = values['-PRECO-']
                cadastratarTipoVeiculo(tipo, preco)
                [sg.popup('Cadastrado com sucesso !', text_color="#04BEB3")]





        return self.janela
