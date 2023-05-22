#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
'''
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        '''

horas = int(input('Quantas horas trabalhadas no mês: '))
valor_hora = float(input('Valor da hora: '))

salario_burto = horas * valor_hora

ir = 0
inss = 10
fgts = (salario_burto * 11 / 100)
sindicato = 3
total_disconto = 0

def retorno_desconto():
    total_disconto = ((salario_burto * ir) / 100) + ((salario_burto * inss) / 100)
    print(f'Salário Bruto: ({horas}h * {valor_hora}R$)  : R$ {salario_burto}')
    print(f'(-) ir ({ir}%)                    : R$ {((salario_burto * ir) / 100)}')
    print(f'(-) INSS ({inss}%)                 : R$ {((salario_burto * inss) / 100)}')
    print(f'FGTS (11%)                     : R$ {fgts}')
    print(f'Total de descontos             : R$ {total_disconto}')
    print(f'Salario Liquido                : R$ {salario_burto - total_disconto - fgts}')

if salario_burto < 900:
    retorno_desconto()
    
    # como o print repete varias vez fica mais facil jogar numa função

    #total_disconto = ((salario_burto * ir) / 100) + ((salario_burto * inss) / 100)
    #print(f'Salário Bruto: ({horas}h * {valor_hora}R$)  : R$ {salario_burto}')
    #print(f'(-) ir ({ir}%)                    : R$ {((salario_burto * ir) / 100)}')
    #print(f'(-) INSS ({inss}%)                 : R$ {((salario_burto * inss) / 100)}')
    #print(f'FGTS (11%)                     : R$ {fgts}')
    #print(f'Total de descontos             : R$ {total_disconto}')

elif salario_burto < 1500:
    ir = 5
    retorno_desconto()

elif salario_burto < 2500:
    ir = 10
    retorno_desconto()

else:
    ir = 20
    retorno_desconto()
