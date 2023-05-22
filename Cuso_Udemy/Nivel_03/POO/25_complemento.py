# decorador

def meu_repr(self):
    class_name = self.__class__.__name__ # pegando o nome da class
    class_dict = self.__dict__ # dicionario
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


class Jogo:
    def __init__(self, nome):
        self.nome = nome

a = Jogo('LOL')

print(Jogo('LOL'))   # mostrando o endereço na memoria     
print(a.nome) # usando o .nome da class e possivel ver o nome em vez da memoria

@adiciona_repr
class Iten:
    def __init__(self, nome):
        self.nome = nome


print(Iten('Gume'))