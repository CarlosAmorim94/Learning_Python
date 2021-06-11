sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F' :
    sexo = str(input('Dados inválidos, digite seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))