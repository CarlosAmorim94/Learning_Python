"""
EXERCÍCIO 052: Números Primos
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

#Coleta de dados
numero = int(input('Digite um número: '))

#Repetição de números
c = 0
tot = 0
for c in range(0, numero):
        c += 1
        if numero % 1 == 0 and numero % c == 0:                     #Verificando núeros primos
            print('\33[32m{}\33[m'.format(c), end=' ')              #Primos em verde
            tot += 1
        else:
            print('\33[31m{}\33[m'.format(c), end=' ')              #Não primos em vermelho

print('\nO número {} foi divisível {} vezes'.format(numero , tot ))
if tot == 2:
    print('Por isso ele É PRIMO')
else:
    print('por isso ele NÃO É PRIMO')