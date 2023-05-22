#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input('Numero: '))

if num < 0:
    print('Numero negativo.')

elif num == 0:
    print('Numero neutro')

else:
    print('Numero possitivo.')    