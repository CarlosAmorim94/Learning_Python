"""
EXERCÍCIO 012: Calculando Descontos
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

p = float(input('Dgite o valor do produto R$'))
d = p - (p * 0.05)
print('O valor R${} com um desconto de 5%\nO valor a ser pago será R${:.2f}'.format(p,d))