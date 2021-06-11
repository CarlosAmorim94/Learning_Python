from time import sleep

n = int(input('Digite um número para contagem regressiva: '))
for cont in range(10, -1, -1):
    sleep(1)
    print(cont)
print('ACABOU!!')