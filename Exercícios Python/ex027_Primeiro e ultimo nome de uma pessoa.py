  
"""
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('O seu primeiro nome é {}\n O ultimo é {}'.format(nome[0], nome[len(nome)-1]))