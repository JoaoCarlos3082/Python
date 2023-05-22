# Metodos e instâncias em python

class Carro():
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self): # METEDO | ação | Movimento
        print(f'O {self.nome} esta acelerrando.')

carro_01 = Carro('Celta')
print(carro_01.nome)
carro_01.acelerar()

print('')

carro_02 = Carro('Ford')
print(carro_02.nome)
carro_02.acelerar()