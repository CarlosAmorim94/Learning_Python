"""
EXERCÍCIO 047: Contagem de Pares
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""

for count in range(0,51,2):
    if count % 2 == 0:
        print(count, end = ' ')
print('FIM')