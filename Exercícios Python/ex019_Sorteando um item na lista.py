"""
EXERCÍCIO 019: Sorteando um Item na Lista
Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""

from random import choice

a1 = input('Digite o nome do 1º aluno: ')
a2 = input('Digite o nome do 2º aluno: ')
a3 = input('Digite o nome do 3º aluno: ')
a4 = input('Digite o nome do 4º aluno: ')
lista = [a1, a2, a3, a4]

print('O aluno escolhido para apagar a lousa é {}'.format(choice(lista)))