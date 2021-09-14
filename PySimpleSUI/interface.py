
import PySimpleGUI as sg

#Tema
sg.theme('Reddit')
#Layout
layout = [
    [sg.Text('Digite um número:')],
    [sg.Input()],
    [sg.OK()],
]
#Janela
janela = sg.Window('Teste', layout)
#Leitura dos valores da tela
