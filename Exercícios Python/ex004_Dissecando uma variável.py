txt = input('Digite algo:')

print('O tipo primitivo de {} é {}'.format(txt, type(txt)))
print('{} só tem espaços? {}'.format(txt, txt.isspace()))
print('{} é um número? {}'.format(txt, txt.isnumeric()))
print('{} é alfabético? {}'.format(txt, txt.isalpha()))
print('{} é alfanumérico? {}'.format(txt, txt.isalnum()))
print('{} está em maiúsculas? {}'.format(txt, txt.isupper()))
print('{} está em minúsculas? {}'.format(txt, txt.islower()))
print('{} está capitalizada? {}'.format(txt, txt.istitle()))