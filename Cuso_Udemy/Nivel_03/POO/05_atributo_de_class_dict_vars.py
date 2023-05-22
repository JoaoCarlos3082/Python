# Atributo da Class

import datetime

ano = datetime.datetime.now().year

class Pessoa:
    ano_atual = ano # Atributo da class

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def data_de_nascimento(self):
        return Pessoa.ano_atual - self.idade            

pessoa01 = Pessoa('João', 19)
print(pessoa01.data_de_nascimento())

print()

pessoa02 = Pessoa('Renato', 20)
print(pessoa02.data_de_nascimento())

# __dict__ montra um disionarios com os valores da class
# vars --> ele chama o __dict__

print(pessoa01.__dict__)
print(vars(pessoa01))