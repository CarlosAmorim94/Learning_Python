
import PySimpleGUI as sg

#Tema
sg.theme('Reddit')
#Layout
layout = [
    [sg.Text('Digite seu nome:')],
    [sg.Input(key='nome')],
    [sg.Text('Digite sua idade:')],
    [sg.Input(key='idade')],
    [sg.OK(), sg.Cancel(), sg.Button('Enviar dados', key='enviar_dados'),sg.Text(key='acesso', size=(20,1))],
]
#Janela
janela = sg.Window('Teste', layout)
#Leitura dos valores da tela
while True:
    evento, valores = janela.Read()
    if evento == sg.WIN_CLOSED:
        sg.popup('Obrigado por utilizar o sistema!\nBy: Carlos Vezza' , custom_text=('Continuar' , 'Sair'))
        break;
    if evento == 'OK':
        print('O seu nome é {} e sua idade é {}'.format(valores['nome'], valores['idade']))
        if int(valores['idade']) >= 18 :
            janela['acesso'].update('Acesso Concedido')
        else:
            janela['acesso'].update('Acesso Negado')
            janela['enviar_dados'].update(disabled=True)
            janela['nome'].update(text_color='red')
janela.close()