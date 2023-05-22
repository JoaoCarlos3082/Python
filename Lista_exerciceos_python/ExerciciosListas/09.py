# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

numeros = []
quadaro = []

for i in range(4):
    numero = int(input(f'Numero {i}: '))
    numeros.append(numero)

for i in range(len(numeros)):
    quadaro.append(numeros[i]**2)

print(quadaro)    
