

def criar_multiplicador(x):
    def multiplicar(valor):
        return x * valor
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadraplicar = criar_multiplicador(4)

print(duplicar(10))
print(triplicar(3))
print(quadraplicar(9))