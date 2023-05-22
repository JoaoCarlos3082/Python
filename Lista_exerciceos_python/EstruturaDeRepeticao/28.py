# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.


quantidade_cd = int(input('Quantidades CDs: '))
total = 0

for i in range(1, quantidade_cd+1):
    valor_cd = float(input(f'Valor do CD {i}: '))

    total = total + valor_cd

media_total = total / quantidade_cd    

print(media_total)