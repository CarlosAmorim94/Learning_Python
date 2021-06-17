"""
EXERCÍCIO 031: Custo da Viagem
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
"""

d = float(input('Digite a distância da sua viagem em km: '))
if d>= 200:
    print('O preço da sua passagem será R${:.2f}'.format(d*0.45))
else:
    print('O preço da sua passagem será R${:.2f}'.format(d * 0.50))

print('Tenha uma boa viagem! :-)')