"""
EXERCÍCIO 068: Jogo do Par ou Ímpar
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
win = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador} com um total de {total}', end=' ')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu! Parabéns!!!')
            win += 1
        else:
            print('Você perdeu, tente de novo!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu! Parabéns!!!')
            win += 1
        else:
            print('Você perdeu, tente de novo!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {win} vezes.')