n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('O seu primeiro nome é {}\n O ultimo é {}'.format(nome[0], nome[len(nome)-1]))