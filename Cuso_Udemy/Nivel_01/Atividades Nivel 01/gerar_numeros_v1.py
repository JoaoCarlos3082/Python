import random

for i in range(10):
    print(random.randint(0,3))


numeros = ''

for c in range(9):
    numeros += str(random.randint(0, 9))

print(numeros)    