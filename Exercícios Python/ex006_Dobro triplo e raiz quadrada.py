"""
EXERCÍCIO 006: Dobro, Triplo, Raiz Quadrada
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

n = int(input('Digite um valor: '))
print('O numero escolhido foi {}\n O dobro é {}\n O triplo é {}\n A raiz quadrada é {:.3f}'.format(n, (n * 2), (n * 3), (n ** (1 / 2))))