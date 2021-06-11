#nome = str(input('Qual o seu nome?: '))
#if nome == 'Gustavo':
  #  print('Que que nome lindo vc tem :-)')
#else:
 #   print('Seu nome é tão normal...')
#print('Bom dia {}!'.format(nome))

p1 = float(input('Digite a nota da P1: '))
p2 = float(input('Digite a nota da P2: '))
m = (p1+p2)/2

print('A sua média foi {:.2f}'.format(m))
if m >= 6:
    print('Parabens! Você foi aprovado!')
else:
    print('Que pena! precisa estudar um pouco mais')

print('---FIM---')
