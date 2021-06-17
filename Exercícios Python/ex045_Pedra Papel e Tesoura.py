"""
EXERCÍCIO 045: Pedra, Papel e Tesoura
Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint
from time import sleep

#Cabeçalho
print('\33[1;36m-='*20)
print('                JOKENPÔ!')
print('-='*20)
print('''\33[mEscolha um número:
[ 0 ] = Pedra
[ 1 ] = Papel
[ 2 ] = Tesoura
''')

#jogadas
itens = ('Pedra' , 'Papel' , 'Tesoura')
jogador = int(input('Escolha a sua jogada!: '))
computador = randint(0,2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)

print('-=' * 11)
print('O Jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))
print('-=' * 11)

if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('Jogada inválida!')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('Jogada inválida!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')

#Rodapé FIM
print('\33[1;36m-='*20)
print('                FIM')
print('-='*20)