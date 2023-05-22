# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# primeiro forma
print('primeiro forma')
print()
def zipper(lista1, lista2):
    menor_lista = min(len(lista1), len(lista2))# 'MIN' pega o menor valor entre dois paramentros, no caso pegando o menor valor entre duas lista
    #return [i for i in range(menor_lista)] # usa lista compresion para pegar os indices
    return [(lista1[i], lista2[i]) for i in range(menor_lista)]# colocancod entre parenteses para transformar em uma tupla.

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1, l2))
print()
print()

# segunda forma
from itertools import zip_longest

print('segunda forma')
print()

print(zip(l1, l2))# zip usa o valor da menor lista mostrando o valor na memoria
print(list(zip(l1, l2)))# zip usa o valor da menor lista transformando em uma lista
print(list(zip_longest(l1, l2)))# zip_longest pegar o valor da maior lista