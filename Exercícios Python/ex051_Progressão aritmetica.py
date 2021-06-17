"""
EXERCÍCIO 051: Progressão Aritmética
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for c in range (primeiroTermo , (razao*10), razao ):
    primeiroTermo += razao
    print('{}'.format(primeiroTermo) , ' --> ', end=' ')
print('ACABOU!')