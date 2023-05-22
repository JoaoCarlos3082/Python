# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

maior = 0

menor = 9999999999999

for i in range(5):
    num = int(input('Numero: '))

    if num > maior:
        maior = num

    if num < menor:
        menor = num

print(maior, menor)             