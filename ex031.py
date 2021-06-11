d = float(input('Digite a distância da sua viagem em km: '))
if d>= 200:
    print('O preço da sua passagem será R${:.2f}'.format(d*0.45))
else:
    print('O preço da sua passagem será R${:.2f}'.format(d * 0.50))

print('Tenha uma boa viagem! :-)')