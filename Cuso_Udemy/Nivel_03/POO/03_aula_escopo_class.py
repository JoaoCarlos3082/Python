# escopo da class


class Animal:
    #variavel = '123'

    def __init__(self, nome):
        self.nome = nome
    
    def andar(self):
        return f'{self.nome}, esta andando'
    
    def alimentar(self, alimento):
        self.alimento = alimento
        return f'{self.nome} esta comendo {self.alimento}'

#print(variavel) # erro devido que a variavel esta protegida pelo escopo da class

cachorro = Animal('Cachorro')
print(cachorro.nome)
print(cachorro.andar())
print(cachorro.alimentar('Abacaxi'))
