"""
EXERCÍCIO 033: Maior e Menor Valores
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('digite o terceiro número: '))

# Verificando o menor

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))

# Verificando o maior valor
maior = a
if b > a and c > a:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número digitado foi {}'.format(maior))