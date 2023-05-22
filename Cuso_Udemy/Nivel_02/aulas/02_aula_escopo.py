"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.

"""

x = 10 # local
b = 3

def escopo():
    
    x = 31 #local
    global b
    b = 31
    def outro_escopo():
        x = 41
        print(x)
    outro_escopo()    
    print(x)


print(f'local {x}')
print(f'local {b}')
escopo()# local
print(f'local {x}')
print(f'global {b}')



