"""
EXERCÍCIO 034: Aumentos Múltiplos
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""

s = float(input('Digite seu salário: R$'))
if s > 1250:
    a = (s * 10 / 100) + s
    print('O seu salário será {:.2f}'.format(a))
else:
    a = (s * 15 / 100) + s
    print('O seu salário será {}'.format(a))