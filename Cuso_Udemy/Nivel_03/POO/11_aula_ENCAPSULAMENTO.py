# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções

# ISSO E UMA REGRA DO PYTHON, PARA NOIS 'DEVS'

#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        # publico, pode ser usado em qualquer lugar do codigo.
        self.public = 'publico'

        # '_' e um protected
        # so deve ser usado dentro da class ou da subclass
        self._pretected = 'protegido'

        # '__' e private
        # so deve ser usado dentra da class que foi criada
        self.__private = 'privado'
        
        # publico.
    def metudo_publico(self):
        print(self.__private)
        self.__metudo_private()
        return 'metudo_publico' 

        # protected
    def _metudo_protected(self):
        return '_metudo_protected'  

        # privado
    def __metudo_private(self):
        print('__metudo_private')
        return '__metudo_private'

publc_protected_private = Foo()
#print(publc_protected_private.public)
print(publc_protected_private.metudo_publico())

print('')

print(publc_protected_private._pretected)
print(publc_protected_private._metudo_protected())

print('')

# não e possivel acessar fora da class
 
#print(publc_protected_private.__private)
#print(publc_protected_private.__metudo_private())