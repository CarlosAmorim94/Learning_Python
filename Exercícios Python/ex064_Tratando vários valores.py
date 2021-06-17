"""
EXERCÍCIO 064: Tratando Vários Valores v1.0
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
"""

#Variáveis
n = int(input('Digite um valor [Digite 999 para parar] : '))
quantnum = 0
soma = n

#Resolução
while n != 999:
    n = int(input('Digite um valor [Digite 999 para parar] : '))
    quantnum += 1
    soma += n
    
print('Foram digitados {} numeros e a soma deles é {}'.format((quantnum), (soma - 999)))