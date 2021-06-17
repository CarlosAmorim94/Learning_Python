"""
EXERCÍCIO 018: Seno, Cosseno e Tangente
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import sin,cos,tan,radians

ang = (float(input('Digite um ângulo: ')))
seno = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {} tes o SENO {:.2f}, COSSENO {:.2f} e TANGENTE {:.2f}.'.format(ang,seno,cos,tang))