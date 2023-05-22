# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class Caneta:
    def __init__(self, cor):
        # private protected
        self._cor = cor # Ja chama o SETTER no INIT, devido que estou estancionado o mesmo obejeto
        
        # Atributos que começar com um ou dois underlines
        # não devem ser usados fora da classe.
        self._cor_tampa = None # Configura direto

    # obeter o valor
    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

    # configurar o valor
    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul') # definido a cor
caneta.cor = 'Rosa' # colocando um novo valor, ou seja ele vai para o SETTER(configura o valor) e depois vai para o GETTER(obeten o valor) e retorna o novo valor configurado


caneta.cor_tampa = 'Azul'
print(caneta.cor) 

print('')

#print(caneta.cor_tampa)