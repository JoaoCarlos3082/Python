# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

              #Pegando uma class ja existente no python
class MinhaStr(str):

    # Devido a orden de presedencia o upper da class 'MinhaStr' executado primeiro sobrescrevendo o mesmo metudo da class 'str'
    def upper(self):
        print('Sobreposição de METUDO')
        return super().upper() # super() traz o metudo da class 'STR'


# Como a class 'str' faz parte da minha class 'MinhaStr' ele tem tudo que teria na 'str'
#string = MinhaStr('lucas')
#print(string.upper())    


class A:
    valor_a = 'a'

    # tudo que tem na Class A vai para as class abaixo devido que elas herdam
    def __init__(self, atributo):
        self.atributo = atributo


    def metudo(self):
        print('a')

class B(A):
    valor_b = 'b'

    def __init__(self, atributo):
        super().__init__(atributo)

    def metudo(self):
        print('b')

class C(B):
    valor_c = 'c'

    def metudo(self):
        super().metudo() # ---> super(C, self) -> a Class 'C' vai pegar o que tem na Class 'B' devido que a class 'C' herdou a class 'B'
        super(C, self).metudo()
        print() 
             # mas se trocarmos o para super(B, self) -> ele vai pegar o metudo da class 'A' 
        super(B, self).metudo()
        print()
        print('c')

c = C('Valor')

# variavel c que recebe a class C tem todos os valores de A e B devidoq que a class 'C' herda a class 'B' que herda a class 'A'
print(c.valor_a)
print(c.valor_b)
print(c.valor_c)

print()

c.metudo()

