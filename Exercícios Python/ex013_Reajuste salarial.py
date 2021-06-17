"""
EXERCÍCIO 013: Reajuste Salarial
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
(Personalizado: O usuário digita a porcentagem do aumento e salário por hora )
"""

hor = float(input('Digite o valor da sua hora em reais R$'))
por = float(input('Digite a porcentagem do aumento: '))
sal = hor * 220
aum = por/100
print('Seu salário atual é R${:.2f} com {}% de aumento seu salário será R${:.2f}'.format(sal,por,((sal*aum)+sal)))