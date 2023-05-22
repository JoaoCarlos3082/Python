#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.


num1 = int(input('Numero 1: '))

num2 = int(input('Numero 2: '))

if num1 < num2:
    for i in range(num1, num2):
        print(i)

else:
    print(f'Não tem intervalo devido que os numero {num1} e {num2} igual o primeiro numero e menor que o segundo não tendo intervalo')        