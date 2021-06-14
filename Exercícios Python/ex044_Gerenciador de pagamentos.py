#Cabeçalho
print('\33[1;32m-='*20)
print('        Gerenciador de Pagamentos')
print('-='*20)

#Preço
valor = float(input('\33[mDigite o valor da compra: R$'))

#Opções de pagamento
print('''Escolha a condição de pagamento:

[ 1 ] = À Vista no dinheiro ou cheque....... 10% de Desconto
[ 2 ] = À vista no cartão...................  5% de Desconto
[ 3 ] = Parcelado em 2X no cartão........... Preço Normal
[ 4 ] = Parcelado em 3X ou mais no cartão... 20% de Juros
''')

pagamento = int(input('Digite o número da opção de pagamento: '))
if pagamento == 4:
    quant_parcela = int(input('Quantas em quantas parcelas será pago: '))
    valor_parcela = ((valor * 20 / 100) + valor) / quant_parcela
    print('O valor R${:.2f} será dividido em {:.0f} parcelas de R${:.2f}'.format(valor,quant_parcela,valor_parcela))

elif pagamento == 3:
    print('O valor R${} será dividido em 2 parcelas de R${:.2f}'.format(valor,(valor / 2)))

elif pagamento == 2:
    desconto5 = valor - (valor * 5/100)
    print('A compra de R${} terá desconto de 5% e passará a ser R${:.2f}'.format(valor,desconto5))

elif pagamento == 1:
    desconto10 = valor - (valor * 10 / 100)
    print('A compra de R${} terá desconto de 10% e passará a ser R${:.2f}'.format(valor, desconto10))

#Rodapé FIM
print('\33[1;32m-='*20)
print('                FIM')
print('-='*20)
