from cProfile import label
from tkinter import*
from tkinter.constants import E
from turtle import window_height
from PySimpleGUI import PySimpleGUI as sg

root = Tk()

img = PhotoImage(file="img/G.png")

label_image = Label(root, image=img).pack()

##root.mainloop()

sg.theme('DarkTeal')

layout = [
    [sg.Text('Funcionario(a)'), sg.Input(key='funcionario',  size=(25, 1))],
    [sg.Text('Matricula'), sg.Input(
        key='matricula', password_char='*', size=(25, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]

]

janela = sg.Window('Acesso ao Sistema EG', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['funcionario'] == 'João Gomes Tedesco' and valores['matricula'] == 'JGT1478':
            print('Acesso EG Estacionamento Rotativo')
