#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto_01 = float(input('Preço do prdouto 01: '))
produto_02 = float(input('Preço do prdouto 02: '))
produto_03 = float(input('Preço do prdouto 03: '))

menor = produto_01

if produto_02 < menor:
    menor = produto_02

if produto_03 < menor:
    menor = produto_03

print(f'O produto que você deve comprar é o {menor}R$')    
