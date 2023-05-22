# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.


while True:
    n = int(input('numero: '))

    if n % 2 == 1:
        print(f'Numero {n} é impar.')

    else:
        print(f'Numero {n} é par')    