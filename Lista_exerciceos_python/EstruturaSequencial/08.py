#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Valor da sua hora: '))

hora_trabalhada = float(input('Horas Trabalhadas: '))

print(f'Você trabalha {hora_trabalhada}h por dia e ganha {valor_hora}R$ por hora trabalha, tendo o total de {hora_trabalhada * valor_hora}R$ no dia.')