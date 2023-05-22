# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos(propriedades entre outros nomes) e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase (primeira letra e MAISCULA) para nomes de
# classes.

# Criar a class
class Pessoa():  
    def __init__(self, nome, sobrenome): # __INIT__ inicializa os ATRIBUTOS DA CLASS | sempre tem o 'SELF' | Pasando os parametros
        self.nome = nome # 'SELF.' referencia | criando ATRIBUTOS
        self.sobrenome = sobrenome # 'SELF.' referencia | criando ATRIBUTOS
        

#criando a estancia da p1
    #chamando a class   
p1 = Pessoa('Carlos', 'Sobrenome') # criar obejeto | SELF já e automaticamente passado

#instâncias da class
#p1.nome = 'Carlos'
#p1.sobrenome = 'Matheus'

p2 = Pessoa('Pedro', 'Henrique') # criar obejeto | SELF já e automaticamente passado

#p2.nome = 'Pedro'
#p2.sobrenome = 'Henrique'

print(p1.nome)
print(p1.sobrenome)
print()
print(p2.nome)
print(p2.sobrenome)