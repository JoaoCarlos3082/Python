# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
v1 = [1, 2, 3 ,4 ,5, 6]

v2 = [7, 8, 9, 10, 11, 12]

v3 = [13, 14, 15 ,16, 17, 18]

v4 = []

for i in range(len(v1)):
    v4.append(v1[i])
    v4.append(v2[i])
    v4.append(v3[i])

print(v4)    
     