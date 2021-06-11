car = float(input('Quantos dias de aluguel? : '))
km = float(input('Quantos Km foram rodados? : '))
print('O total a ser pago é de R${:.2f}'.format((car*60)+(km*0.15)))
print('Valor dos dias é R${}\nValor dos Km é R${}'.format((car*60),(km*0.15)))

