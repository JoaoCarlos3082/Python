'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

'''

ano_atual = 2023

salario = float(input('Salario: '))
salario_final = 0

data_da_adimisao = int(input('Admisão: '))

valor_range = ano_atual - data_da_adimisao

aumento = 1.5
aumento_final = 0

for i in range(valor_range):
    aumento_final = aumento * i
    salario_final = salario + ((salario * aumento_final) / 100)

print(aumento_final)  
print(salario_final)  
    