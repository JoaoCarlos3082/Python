#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Altura em Cm: '))

metro_altura = altura / 100

peso = (72.7 * metro_altura) - 58

print(f'O pesso ideal de uma pesso com {metro_altura}m é {peso:.2f}Kg')