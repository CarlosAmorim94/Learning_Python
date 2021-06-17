"""
EXERCÍCIO 054: Grupo de Maioridade
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

#Importações
from datetime import date

#Variáveis
ano = date.today().year
me = 0
ma = 0

#Resolução
for pess in range( 1 , 8 ):
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = ano - nascimento
    if idade < 18:
        me += 1
    else:
        ma += 1
print('''Menores de idade = {}
Maiores de idade = {}'''.format( me , ma ))