# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
par = []
impar = []

for i in range(5):
    num = int(input(f'Numero {i}: '))
    numeros.append(num)

    if num % 2 == 0:
        par.append(num)
        
    else:
        impar.append(num)    


print(numeros)
print(par)
print(impar)        