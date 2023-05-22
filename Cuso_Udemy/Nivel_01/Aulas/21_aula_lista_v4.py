"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

-------------------------

.COPY() --> copia a lista

"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a # lista "b" esta apontando para a lisa "a"
print('Printe da lista "b" apontado para a lista "a": ',lista_b)

lista_b = lista_a.copy() # copei a lista

lista_a[0] = 'Monster'
print('Printe da lista "a": ',lista_a)
print('Printe da copia da lista "a" na lista "b": ',lista_b)