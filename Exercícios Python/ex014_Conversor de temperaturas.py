"""
EXERCÍCIO 014: Conversor de Temperaturas
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""

cel = float(input('Digite a temperatura em grau Celsius(ºC) :'))
far = (cel * 1.8) + 32
print('{}ºC convertido em Fahrenheit ficará {}ºF'.format(cel,far))