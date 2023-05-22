# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

par = []
impar = []

for i in range(5):
    num = int(input(f'Numero {i+1}: '))

    if num % 2 == 0:
        par.append(num)

    else:
        impar.append(num)

print(par)
print(impar)            
    