"""
EXERCÍCIO 038: Comparando Números
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
"""

#Imports:
from datetime import date

#Coleta de dados:
nasceu = int(input('Digite o seu ANO de nascimento (ex:1994): '))

#Variáveis:
atual = date.today().year
idade = atual - nasceu
maidade = nasceu + 18

print('Quem nasceu em {} terá {} anos em {}'.format(nasceu, idade, atual))

#Comparando:
if idade > 18:
    print('Já passou do tempo de se alistar! Deveria ter se alistado há {} anos atrás!'.format(atual - maidade))

elif idade == 18:
    print('Você está no ano de alistamento! Procure o exército')

else:
    print('Ainda está cedo para se alistar! O alistamento deverá ser feito em {} anos'.format((atual - maidade)*-1))