#Um posto está vendendo combustíveis com a seguinte tabela de descontos:

'''
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

'''

opc = input('Gasolina[G] R$ 2,50. ou Alcol R$ 1,90. [A]: ')[0].strip()

litros = int(input('Quantos litros: '))

gasolina = litros * 2.50
alcol = litros * 1.90

if opc in 'Gg':
    if litros > 20:
        print(f'O total com {litros}L gasolina deu {gasolina}R$, mas com o desconto de 6% deu { gasolina - ((gasolina * 6) / 100)}')
    else:
        print(f'O total com {litros}L gasolina deu {gasolina}R$, mas com o desconto de 4% deu { gasolina - ((gasolina * 4) / 100)}') 

if opc in 'Aa':
    if litros > 20:
        print(f'O total com {litros}L alcol deu {alcol}R$, mas com o desconto de 6% deu { alcol - ((alcol * 5) / 100)}')
    else:
        print(f'O total com {litros}L alcol deu {alcol}R$, mas com o desconto de 4% deu { alcol - ((alcol * 3) / 100)}') 