#Variáveis
n = int(input('Digite um valor [Digite 999 para parar] : '))
quantnum = 0
soma = n

#Resolução
while n != 999:
    n = int(input('Digite um valor [Digite 999 para parar] : '))
    quantnum += 1
    soma += n
    
print('Foram digitados {} numeros e a soma deles é {}'.format((quantnum), (soma - 999)))
