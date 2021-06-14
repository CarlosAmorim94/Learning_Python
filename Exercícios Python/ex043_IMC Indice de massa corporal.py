#Cabeçalho
print('\33[1;34m-='*20)
print('           Cálculo de IMC')
print('      (Índice de Massa Corporal)')
print('-='*20)

#Coleta de dados
peso = float(input('\33[mQual é seu peso? (Kg): '))
altura = float(input('Qual é a sua altura (M): '))

#Resolução
imc = peso / (altura**2)
print('o seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('IMC {:.1f} é considerado ABAIXO DO PESO'.format(imc))

elif 18.5 <= imc < 25:
    print('IMC {:.1f} é considerado PESO IDEAL'.format(imc))

elif 25 <= imc < 30:
    print('IMC {:.1f} é considerado SOBREPESO'.format(imc))

elif 30 <= imc < 40:
    print('IMC {:.1f} é considerado OBESIDADE'.format(imc))

else:
    print('IMC {:.1f} é considerado OBESIDADE MÓRBIDA'.format(imc))

#Rodapé FIM
print('\33[1;34m-='*20)
print('                FIM')
print('-='*20)
