s = float(input('Digite seu salário: R$'))
if s > 1250:
    a = (s * 10 / 100) + s
    print('O seu salário será {:.2f}'.format(a))
else:
    a = (s * 15 / 100) + s
    print('O seu salário será {}'.format(a))
