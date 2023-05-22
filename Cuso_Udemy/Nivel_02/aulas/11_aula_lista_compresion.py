# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# - criando uma lista -
lista = []
for numero in range(11):
    lista.append(numero)
print(lista)


# - Lista compresion -
lista_2 = [numero_2 for numero_2 in range(11)]
print(lista_2)


lista_3 = [numero_3 * 2 for numero_3 in range(11)]
print(lista_3)
