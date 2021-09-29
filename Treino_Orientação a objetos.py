from random import randint

class Pessoa:

    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        #self._sexo = sexo          #Parâmetro protegido por causa do _ (Se estivesse no código, seria indetectável e imutável)
        #self._altura = altura      #Parâmetro protegido por causa do _ (Se estivesse no código, seria indetectável e imutável)
    
    @classmethod
    def ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def numero_aleatorio():
        gerador = randint(1, 999)
        return gerador

#carlos = Pessoa('Carlos', 27, 'M', 1.69) #instanciando um objeto normal
danielle = Pessoa.ano_nascimento('Danielle', 1990) #instanciando parametros fora da classe, fora do construtor

print(f'A idade de {danielle.nome} é {danielle.idade} anos') #Método de classe fora da classe 
print(f'Um número aleatório: {Pessoa.numero_aleatorio()}')  #Função sem self
print(f'O ano atual é {danielle.ano_atual}') #Atributo da classe

Pessoa.ano_atual = 2022
print(f'O ano atual é {danielle.ano_atual}') #Alterando um atributo da classe
