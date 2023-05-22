# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120


n = int(input('Numero: '))

fatorial = 1

for i in range(n):
    fatorial *= (i + 1)

print(fatorial)    