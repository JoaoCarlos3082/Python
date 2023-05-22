# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tel

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None


    # Configurando o motor e fabricante

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor      

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante     

class Motor:   
    def __init__(self, nome):
        self.nome = nome

class Fabricante:        
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Gol 2011') # tipo do carro
# configurações desse caro
gol = Fabricante('GOL')
motor_2_0 = Motor('2.0')
fusca.fabricante = gol
fusca.motor = motor_2_0

print(fusca.nome, fusca.motor.nome, fusca.fabricante.nome)
print()

classic = Carro('Classic 2011')

honda = Fabricante('Honda')
motor_2_0 = Motor('1.0')
classic.fabricante = honda
classic.motor = motor_2_0

print(classic.nome, classic.motor.nome, classic.fabricante.nome)
print()
