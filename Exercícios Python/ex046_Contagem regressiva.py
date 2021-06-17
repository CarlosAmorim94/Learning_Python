"""
EXERCÍCIO 046: Contagem Regressiva
Faça um programa que mostre na tela uma contagem regressiva para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

from time import sleep

n = int(input('Digite um número para contagem regressiva: '))
for cont in range(n, -1, -1):
    sleep(1)
    print(cont)
print('ACABOU!!')