from tkinter.constants import E
from turtle import window_height
from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkTeal')

layout = [
    [sg.Text('Funcionario(a)'), sg.Input(key='funcionario',  size=(50,50))],
    [sg.Text('Matricula'),sg.Input(key='matricula', password_char='*', size=(50,50))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]

]

janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['funcionario'] == 'João Gomes Tedesco' and valores ['matricula'] == 'JGT1478':
               print('Acesso EG Estacionamento Rotativo')