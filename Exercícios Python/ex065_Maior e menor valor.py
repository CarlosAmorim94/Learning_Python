continuar = 's'
soma = quant = media = maior = menor = 0

while continuar in 'Ss':
    n = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N]: ')).strip()[0]
    soma += n
    quant += 1
    
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / quant
print('O maior número é {} o menor é {} e a média entre eles é {}'.format(maior, menor, media))