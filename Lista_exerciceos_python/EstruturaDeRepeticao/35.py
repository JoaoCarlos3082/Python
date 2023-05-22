# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.


primos = []

numeros_primos = int(input('Numeros primos de 1 ate: '))

for i in range(numeros_primos+1):
    if i % 2 == 1:
        primos.append(i)

print(primos)        

