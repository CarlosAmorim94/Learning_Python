"""
EXERCÍCIO 049: Tabuada v2.0
Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
"""

n = int(input('Digite um número para a tabuada: '))
for c in range(1 , 11):
    print('{} X {:>2} = {:2}'.format(n, c, (n * c)))