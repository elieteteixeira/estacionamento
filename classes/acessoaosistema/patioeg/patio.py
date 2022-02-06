from tkinter import N, font
from turtle import color
from PySimpleGUI import PySimpleGUI as sg


def home():
    sg.theme = 'black'

    flayout = [
        [sg.Text('Quantidade de Vagas')],
        [sg.Button('ddrre')],
        [sg.Text('')],
        [sg.Button('sair')]

    ]

    janela = sg.Window('Estacionamento EG Rotativo', flayout, size=(400, 300), element_justification='center')

    button, Values = janela.Read()

    if button == 'VVV':
        janela.classe()

    if button == 'SSS':
        janela.exit()


home()

flayout1 = [

    [sg.Text('O Estacionamento EG Rotativo, foi fundado em 1995, por Eliete Teixeira e Gerlande XXXXX, \n'
             'Hoje com 27 anos de trabalho em equipe com um quadro de funcionários excelente. \n' 
             'Temos orgulho de dizer que valeu apena cada esforço vivido.\n' 'Obrigada!')],

    [sg.Button('Voltar')]

]

janela1 = sg.Window('Agradecimentos', flayout1, size=(600, 300), text_justification='center')
button, values = janela1.read()

if button == 'Voltar':
    janela1.Close()

    home()




