#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, #baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input('Salario: '))
aumento_por_cem = 0


if salario <= 280:
    aumento_por_cem = 20

elif salario <= 700:
    aumento_por_cem = 15

elif salario <= 1500:
    aumento_por_cem = 10

elif salario > 1500:
    aumento_por_cem = 5    

print(f'O salario de {salario}R$ teve um aumento de {aumento_por_cem}%, tendo um aumento de {(salario * aumento_por_cem) / 100}, com o salario final de {salario + (((salario * aumento_por_cem)) / 100)}')    