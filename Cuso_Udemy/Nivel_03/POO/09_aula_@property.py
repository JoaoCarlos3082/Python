
# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

# Property e um METUDO que se comprta como um ATRIBUTO

# GET
class Caneta:
    def __init__(self, cor):

        # caso alterar o nome SELF.COR para SELF.COR_DA_CANETA, darria erro no codigo cliente devido que ele teria que fazer alteração no proprio codigo devido a usar o antigo nome
        
        #self.cor = cor
        
        self.cor_da_caneta = cor
    
    # poderiamos usar o get para corrigir o problema agora podendo trocar os nomes sem ter problemas com o codigo cliente
    def get_cor(self):
        return self.cor_da_caneta

caneta = Caneta('Preto')
print(caneta.get_cor())
print(caneta.get_cor())

print()

# PROPERTY
class Lapis:
    def __init__(self, cor_lapis):

        self.cor_lapis = cor_lapis

    # usando o property o metodo no codigo cliente se comporta como com um atributo
    # ou seja na class ele e um MÉTODO mas no codigo ele e um ATRIBUTO
    @property
    def cor(self):
        return self.cor_lapis
    
lapis = Lapis('Verde')
print(lapis.cor)
print(lapis.cor)

    
        

