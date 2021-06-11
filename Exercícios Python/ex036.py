# Perguntas:
val = float(input('Qual o valor do imóvel desejado? R$'))
sal = float(input('Qual o valor do seu salário? R$'))
temp = int(input('Em quantos anos deseja pagar? '))

#Variaveis:
parc = val / (temp * 12)
ps = sal * 30 / 100

#Resolução:
print('A parcela será R${:.2f}'.format(parc))
print('Será pago em {} anos ({} meses).'.format(temp,(temp * 12)))

if parc <= ps:
    print('\033[1;32mParabéns! O seu empréstimo foi aceito!\033[m')

else:
    print('\033[1;31mO seu empréstimo infelizmente foi negado.\033[m')

print('-----------FIM-----------')




