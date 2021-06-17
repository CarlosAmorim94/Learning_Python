"""
EXERCÍCIO 035: Analisando Triângulo v1.0
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""

#Cabeçalho
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

#Coleta de dados
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

#Resolução
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('os segmentos acima NÃO PODEM formar um triângulo!')