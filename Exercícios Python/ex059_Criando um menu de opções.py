"""
EXERCÍCIO 059: Criando um Menu de Opções
Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
option = 0

while option != 5:

    print('''
    Escolha a opção:
    [ 1 ] = Somar
    [ 2 ] = Multiplicar
    [ 3 ] = Qual é o maior
    [ 4 ] = Novos números
    [ 5 ] = Sair
    ''')
    print('-=' *20)
    option = int(input('Digite a opção desejada: '))
   
   
    if option == 1: #Somando
        r = n1 + n2
        print('A soma entre {} e {} é igual a {:.0f}'.format( n1, n2, r ))
    elif option == 2: #Mutiplicando
        r = n1 * n2
        print('A multiplicação entre {} e {} é igual a {:.0f}'.format(n1, n2, r))
    elif option == 3: #Qual é o maior
        if n1 > n2:
            print('O maior número digitado foi {}'.format(n1))
        else:
            print('O maior número digitado foi {}'.format(n2))
    elif option == 4: #Novos numeros
        print('Digite os números novamente...')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif option == 5:
        print('Obrigado por utilizar o software, volte sempre!')
    else:
        print('Opção inválida, tente de novo')

print('-=' *20)