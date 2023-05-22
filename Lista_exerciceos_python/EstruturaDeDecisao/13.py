# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


valor = int(input('Valor: '))

if valor == 1:
    print('Domingo')

elif valor == 2:
    print('Segunda')

elif valor == 3:
    print('Terça')

else:
    print('Valor invalido')        