# Faça um programa que leia 5 números e informe o maior número.
maior = 0

for i in range(1, 4):
    num = int(input(f'Numero {i}: '))

    if num > maior:
        maior = num

print(maior)    