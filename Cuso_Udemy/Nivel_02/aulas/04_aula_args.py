'''

args -> argumentos nao nomeados
*args -> empacotamento é desempacotamento

------------------------
def soma(x, y):
    return x + y

print(soma(1, 2))

soma(1, 2, 3)# ERRO na ha variaveis suficientes
'''


def soma(*args):
    total = 0
    for numeros in args:
        total = total + numeros

    return total

print(soma(1, 2, 3, 4, 5, 6))

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))