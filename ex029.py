v = float(input('Digite a velocidade do carro (Km/h): '))
if v >= 81:
    m = (v - 80) * 7
    print('Você ultrapassou a velocidade máxima de 80 Km/h!!!')
    print('Receberá uma multa de R${:.2f}'.format(m))
else:
    print('Está na velocidade adequada!')
    print('Continue dirigindo com segurança!')

