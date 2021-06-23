"""
EXERCÍCIO 067: Tabuada v3.0
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
while True:
    num = int(input('Digte o número para a tabuada: '))
    print('-=' * 15)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-=' * 15)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')