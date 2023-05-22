# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.


v1 = [1, 2, 3 ,4 ,5, 6]

v2 = [7, 8, 9, 10, 11, 12]

v3 = []


for i in range(len(v1)):
    v3.append(v1[i])
    v3.append(v2[i])

print(v3)    
     