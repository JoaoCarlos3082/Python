"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""


#        0  1  2  3   4   5   6
lista = [1, 2, 4, 61, 21, 33, 11]

print(lista[0] + lista[1])

lista[2] = 33

print('print do elemento 2 da lista: ',lista[2])

del lista[2] # deleta um elemento da lista.

print('print do elemento 2 da lista: ',lista[2])

lista.append(900) # adicionar uma valor na ultima possiçao da lista

print('Print da lista: ',lista)

lista.pop() # removo o ultimo elemento da lista

print('Print da lista: ',lista)

lista.insert(0, 111) # insere um dado em um idece da lista

print('Print da lista: ',lista)


