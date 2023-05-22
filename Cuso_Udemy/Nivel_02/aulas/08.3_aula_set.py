# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {1, 2, 4, 5}
s3 = {2, 2, 3, 3, 4, 5}
#s4 = s1 | s2 | s3
s4 = s1.union(s2)
print(s4)
s4 = s1 & s2 
print(s4)
s4 = s1 - s2 
print(s4)
s4 = s1 ^ s2 

print(s4)