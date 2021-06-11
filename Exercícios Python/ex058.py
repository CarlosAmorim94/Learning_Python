from random import randint

print('\33[1;33m-=-\33[m' *20)
print('\33[1;33mVamos jogar? eu pensei em um número, tente advinhar qual é!\33[m')
print('\33[1;33m-=-\33[m' *20)

player = int(input('Digite seu palpite de 0 a 10: '))
pc = randint(0 , 10)
tentativas = 0

while player != pc :
    player = int(input('\33[1;31mErrou!\33[m Digite seu palpite de 0 a 10: '))
    tentativas += 1
    if player > pc :
        print('O meu número é menor que esse!')
    elif player < pc :
        print('O meu número é maior que esse!')
    else:
        print('''
        \33[1;32mVOCÊ ACERTOU!\33[m
        Eu pensei em {}, você chutou {} 
        Tentou {} vezes'''.format( pc , player , (tentativas+1)))

print('\33[33m-=-\33[m' *10)
print('\33[33m             FIM\33[m')
print('\33[33m-=-\33[m' *10)