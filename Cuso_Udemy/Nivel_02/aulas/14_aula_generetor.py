import sys

# Generator expression, Iterables e Iterators em Python
lista = [n for n in range(1000)]# lista esta na memoria 
generator = (n for n in range(1000))# não esta na memoria

print(sys.getsizeof(lista)) #pesso na memoria
print(sys.getsizeof(generator))#pesso na memoria

print(generator)

for n in generator:
   print(n)

'''
vantagens do generetor: possui baixo valor de memoria
desvantags do generetor: ele so sabe o proximo valor, entao não e possivel ver o tamanho da lista, indice etc

vantagen da lista: Mais facil de ser tratada é possui indeces, tamanho etc...
desvantagns da lista: dependando da lista possui alto valor na memoria.

'''   