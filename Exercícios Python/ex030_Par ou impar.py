"""
EXERCÍCIO 030: Par ou Ímpar?
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

n = float(input('Digite um número: '))
r = n % 2
if r == 0:
    print('O número {} é par.'.format(n))
else:
    print('O número {} é impar.'.format(n))