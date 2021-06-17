"""
EXERCÍCIO 015: Aluguel de Carros
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""

car = float(input('Quantos dias de aluguel? : '))
km = float(input('Quantos Km foram rodados? : '))
print('O total a ser pago é de R${:.2f}'.format((car*60)+(km*0.15)))
print('Valor dos dias é R${}\nValor dos Km é R${}'.format((car*60),(km*0.15)))