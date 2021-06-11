primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for c in range (primeiroTermo , (razao*10), razao ):
    primeiroTermo += razao
    print('{}'.format(primeiroTermo) , ' --> ', end=' ')
print('ACABOU!')