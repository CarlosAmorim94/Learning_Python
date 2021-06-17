"""
EXERCÍCIO 029: Radar Eletrônico
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""

v = float(input('Digite a velocidade do carro (Km/h): '))
if v >= 81:
    m = (v - 80) * 7
    print('Você ultrapassou a velocidade máxima de 80 Km/h!!!')
    print('Receberá uma multa de R${:.2f}'.format(m))
else:
    print('Está na velocidade adequada!')
    print('Continue dirigindo com segurança!')