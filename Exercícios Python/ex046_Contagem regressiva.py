from time import sleep

n = int(input('Digite um número para contagem regressiva: '))
for cont in range(n, -1, -1):
    sleep(1)
    print(cont)
print('ACABOU!!')