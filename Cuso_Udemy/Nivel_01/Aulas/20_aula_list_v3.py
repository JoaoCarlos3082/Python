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


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

c = a + b # concatenando a lista
print('Print da lista "a" sem nem uma alteração: ',a)
a.extend(b) # extend a lista com outra lista.
print('Usando o "EXTEND" para extender uma lista no caso a lista "a": ',a)
print('Usando o "+" pra Concatenar as listas: ',c)
