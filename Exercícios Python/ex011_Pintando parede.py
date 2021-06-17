"""
EXERCÍCIO 011: Pintando Parede
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
"""

a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
print('Sua parede mede {}X{} M\nEla tem a área de {:.2f} M²\nSerão necessários {:.2f} litros de tinta para cobrir toda a parede.'.format(a,l,(a*l),((a*l)/2)))