#Faça um Programa que peça dois números e imprima o maior deles.

num_1 = int(input('Numero 01: '))

num_2 = int(input('Numero 02: '))

if num_1 > num_2:
    print(f'Numero {num_1} é mair que {num_2}')

elif num_2 > num_1:
    print(f'Numero {num_2} é mair que {num_1}')

else:
    print(f'Numeros {num_1} é {num_2} são iguais')
