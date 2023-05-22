#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

cont = 1
maior = 0
menor = 9999999999
total_temp = 0

while True:
    temp = float(input(f'Temperatura {cont}: '))
    total_temp += temp

    if temp == 0:
        break
    else:
        cont += 1


    if temp > maior:
        maior =  temp

    if temp < menor:
        menor = temp  

cont = cont - 1

print(maior)
print(menor)
print(total_temp/cont)

