# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while True:

    n = int(input('Numero: '))

    if n <= 16:

        fatorial = 1

        for i in range(n):
            fatorial *= (i + 1)

        print(fatorial)   

    else:
        print('Informe um numero abaixo de 16.')     