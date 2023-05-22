#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#A - Para homens: (72.7*h) - 58
#B - Para mulheres: (62.1*h) - 44.7

altura = float(input('Altura em Cm: '))

metro_altura = altura / 100

peso_M = (72.7 * metro_altura) - 58

peso_F = (62.1 * metro_altura) - 44.7

print(f'O pesso ideal de uma pesso com {metro_altura:.2f}m é {peso_M:.2f}Kg para homens e para mulheres é {peso_F:.2f}Kg.')
