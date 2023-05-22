#Faça um Programa que leia três números e mostre o maior deles.


num_01 = int(input('Numero 01: '))

num_02 = int(input('Numero 02: '))

num_03 = int(input('Numero 03: '))

if num_01 > num_02 and num_01 > num_03:
    print(f'Numero {num_01} é o maior')

elif num_02 > num_01 and num_02 > num_03:
    print(f'Numero {num_02} é o maior')    

elif num_03 > num_01 and num_03 > num_02:
    print(f'Numero {num_03} é o maior')

else:
    print('Numeros iguais')       