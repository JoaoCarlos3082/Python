# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Numero 1: '))

num2 = int(input('Numero 2: '))

soma = num1 + num2

if num1 < num2:
    for i in range(num1, num2):
        print(i)
        soma = soma + i
        print(soma)

print(soma)        
