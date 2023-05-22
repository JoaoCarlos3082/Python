# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)    

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

c1 = Cliente('Lucas')

c1.inserir_endereco('Conjunto Uirapuru', 21)
c1.inserir_endereco('Av Douglas', 99)

c1.listar_endereco()

