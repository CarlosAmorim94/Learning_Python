"""
EXERCÍCIO 060: Cálculo do Fatorial
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

#-----INICIO DO MODO FÁCIL---
#from math import factorial
#n = int(input('digite um número para calcular o seu fatorial: '))
#f = factorial(n)
#print('O fatorial de {} é {}'.format(n,f))
#----FIM DO MODO FÁCIL----

n = int(input('digite um número para calcular o seu fatorial: '))
c = n
f = 1
print('calculando o {}! : '.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('{}'.format(f))