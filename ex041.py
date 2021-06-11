from datetime import date

nascimento = int(input('Digite sua data de nascimento: '))
hoje = date.today().year
idade = hoje - nascimento

print('O atleta tem atualmente {} anos'.format(idade))

if idade <= 9:
    print('O Atleta com {} anos está cadastrado na cadastrado na CATEGORIA MIRIM'.format(idade))

elif idade <= 14:
    print('O Atleta com {} anos está cadastrado na cadastrado na CATEGORIA INFANTIL'.format(idade))

elif idade <= 19:
    print('O Atleta com {} anos está cadastrado na cadastrado na CATEGORIA JUNIOR'.format(idade))

elif idade <= 25:
    print('O Atleta com {} anos está cadastrado na cadastrado na CATEGORIA SÊNIOR'.format(idade))

else:
    print('O Atleta com {} anos está cadastrado na cadastrado na CATEGORIA MASTER'.format(idade))