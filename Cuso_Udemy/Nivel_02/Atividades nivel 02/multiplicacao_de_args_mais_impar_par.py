'''
def multiplicar(*args):
    total = 1
    for numeros in args:
        total = total * numeros
    
    def PrimoPar(total):
        multiplo_de_dois = total % 2 == 0

        if multiplo_de_dois:
            return f'{total} é par'
        return f'{total} é ímpar'
    PrimoPar(total)

print(multiplicar(2, 2, 2, 4, 3))    

'''
def multiplicar(*args):
    total = 1
    for numeros in args:
        total = total * numeros
    return total

def PrimoPar(x):
        multiplo_de_dois = x % 2 == 0

        if multiplo_de_dois:
            return f'{x} é par'
        return f'{x} é ímpar'

print(multiplicar(2, 3, 5, 10, 22))
print(PrimoPar(2))




