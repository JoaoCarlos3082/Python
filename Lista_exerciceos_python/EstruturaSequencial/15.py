#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a- salário bruto.
# b - quanto pagou ao INSS.
# c - quanto pagou ao sindicato.
# e - o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
"""
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""

salario_bruto = float(input('Salario: '))

ir = (salario_bruto * 11) / 100

inss = (salario_bruto * 8) / 100

sindicato = (salario_bruto * 5) / 100

salario_liquido = salario_bruto - ir - inss - sindicato

print('')
print(f'+ Salário Bruto: {salario_bruto}R$\n- IR (11%): {ir}R$\n- INSS (8%): {inss}R$\n= Salário Liquido: {salario_liquido}R$')