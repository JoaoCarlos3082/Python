'''

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''

numero = int(input('Fatorial de: '))

total_fatorial = 1

for i in range(numero,0, -1):
    total_fatorial *= i

print(f"{numero}! = ", end="")

for i in range(numero, 0, -1):
    print(i, end='')
    if i > 1:
        print(' . ', end='')

    else:
        print(' = ', end='')    

print(total_fatorial)


'''
num = int(input("Digite um número inteiro: "))

fatorial = 1

for i in range(1, num+1):
    fatorial *= i

print(f"Fatorial de: {num}")
print(f"{num}! = ", end="")

for i in range(num, 0, -1):
    print(i, end="")
    if i > 1:
        print(" . ", end="")
    else:
        print(" = ", end="")
print(fatorial)'''