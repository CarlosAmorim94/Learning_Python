"""
EXERCÍCIO 028: Jogo da Adivinhação v1.0
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep

print('\33[1;33m-=-\33[m' *20)
print('\33[1;33mVamos jogar? eu pensei em um número, tente advinhar qual é!\33[m')
print('\33[1;33m-=-\33[m' *20)

n = int(input('Digite um número de 0 até 5: '))         #Jogador digita
lista = randint(0,5)                                    #Computador escolhe o número

print('Pensando...')
sleep(2)
if n == lista:
    print('\33[1;32mPARABENS!!! Você acertou!\33[m')
    print('Eu pensei no número {} vc chutou {}'.format(lista, n))
else:
    print('\33[1;31mErrou! haha Tente novamente :-)\33[m')
    print('Eu pensei no número {} vc chutou {}'.format(lista,n))
print('\33[33m-=-\33[m' *10)
print('\33[33m             FIM\33[m')
print('\33[33m-=-\33[m' *10)