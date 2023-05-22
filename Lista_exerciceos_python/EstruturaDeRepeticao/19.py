# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

maior = 0

menor = 9999999999999

for i in range(5):
    num = int(input('Numero: '))

    if num < 1000:

        if num > maior:
            maior = num

        if num < menor:
            menor = num

    else:
        print('Informe um numero entre 0 e 1000')


print(maior, menor) 