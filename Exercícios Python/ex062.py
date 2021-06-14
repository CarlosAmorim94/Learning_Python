primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiroTermo
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quermostrar a mais? '))
print('Progressão finalizada com total de {} termos.'.format(total))