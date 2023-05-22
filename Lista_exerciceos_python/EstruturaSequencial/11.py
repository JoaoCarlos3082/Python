#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#A - o produto do dobro do primeiro com metade do segundo .
#B - a soma do triplo do primeiro com o terceiro.
#C - o terceiro elevado ao cubo.

numero_int_01 = int(input('Numero inteiro 01: '))

numero_int_02 = int(input('Numero inteiro 02: '))

numero_real = float(input('Numero real: '))

print(f'A - {(numero_int_01 * 2) * (numero_int_02/2)}')

print(f'B - {(numero_int_01 * 3) + numero_real}')

print(f'C - {numero_real**3:.2f}')