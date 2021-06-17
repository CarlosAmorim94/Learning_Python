"""
EXERCÍCIO 010: Conversor de Moedas
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.
Considere U$ 1,00 = R$ 3,27
"""

r=float(input('Digite quantos reais você tem na carteira R$'))
print('Você tem R${:.2f}\nConsegue comprar U${:.2f}'.format(r,(r/3.27)),)