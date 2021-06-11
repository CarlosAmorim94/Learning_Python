n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('''
Escolha a opção:
[ 1 ] = Somar
[ 2 ] = Multiplicar
[ 3 ] = Maior
[ 4 ] = Novos números
[ 5 ] = Sair
''')
v = int(input('Digite a opção desejada: '))

while v in(3,1):
    if v == 1:
        r = n1 + n2
        print('A soma entre {} e {} é igual a {:.0f}'.format( n1, n2, r ))
    elif v == 2:
        r = n1 * n2
        print('A multiplicação entre {} e {} é igual a {:.0f}'.format(n1, n2, r))
    elif v == 3:
        if n1 > n2:
            print('O maior número digitado foi {}'.format(n1))
        else:
            print('O maior número digitado foi {}'.format(n2))
if v ==