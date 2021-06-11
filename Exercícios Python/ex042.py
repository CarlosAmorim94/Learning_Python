#Cabeçalho
print('\33[1;33m-='*20)
print('    Analisador de Triângulos')
print('-='*20)

#Coleta de dados
r1 = float(input('\33[mDigite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

#Resolução
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM formar um triângulo!')
    if r1 == r2 == r3:
        print('Triângulos com lados iguais são chamados de triângulos EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triângulos com dois lados iguais são chamados de triângulos ISÓSCELES!')
    else:
        print('Triângulos com lados diferentes são chamados de triângulos ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')

#Rodapé FIM
print('\33[1;33m-='*20)
print('                FIM')
print('-='*20)