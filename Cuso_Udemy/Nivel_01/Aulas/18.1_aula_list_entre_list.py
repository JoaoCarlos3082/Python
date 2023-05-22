#lista dentro de uma lista

lista = [['carlos', 'matheus', 'douglas', 'pedro'], ['Varus', 'Karthus'], ['aatrox', (1,2,3,4,20)]]

#print(lista[0][1], lista[1][0])

#print(lista[2][1][4])

for i in lista:
    for nome in i:
        print(nome)