"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
'''
test = [1, 2, 2, 3, 4, 4, 5, 5]
lista_unica = set(test)
repetidos = set()

for x in lista_unica:
    if test.count(x) > 1:
        repetidos.add(x)

print(repetidos)
'''

l = []
repetidos = set()
primeira_ocorrencia = []
def depulicado(lista_numeros):
    for numero in lista_numeros:
        l.append(numero)
        for x in l:
            if lista_numeros.count(x) > 1:
                repetidos.add(x)
                if len(primeira_ocorrencia) < 1:   
                    if lista_numeros.count(x) > 1:
                        primeira_ocorrencia.append(x)

    if len(repetidos) > 1:            
        print(f'Da lista {l} os numeros {repetidos} são duplicados, {primeira_ocorrencia}')
        l.clear()
        repetidos.clear()
        primeira_ocorrencia.clear()
    else:
         print(f'A lista {l} não tem numerso repetidso {-1}')           

    print()    

for lista in lista_de_listas_de_inteiros:
    depulicado(lista)




