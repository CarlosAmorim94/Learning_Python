maior = 0
menor = 0
for pessoa in range(1 , 6):
    peso = float(input('Digite o peso da {}ª pessoa (Kg): '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('''O maior peso lido foi de {}Kg.
O menor peso lido foi de {}Kg.'''.format( maior , menor ))