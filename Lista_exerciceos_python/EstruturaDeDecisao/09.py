#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input('Numero 01: '))

num2 = int(input('Numero 02: '))

num3 = int(input('Numero 03: '))

numeros = [num1, num2, num3]
                      #organizar os numeros  
numeros_decrescente = sorted(numeros, reverse=True)

print('')
print('sorted')
print('')
print(numeros_decrescente)

print('')
print('com if')
print('')

if num1 >= num2 and num2 >= num3:
    print(num1, num2, num3)
elif num1 >= num3 and num3 >= num2:
    print(num1, num3, num2)
elif num2 >= num1 and num1 >= num3:
    print(num2, num1, num3)
elif num2 >= num3 and num3 >= num1:
    print(num2, num3, num1)
elif num3 >= num1 and num1 >= num2:
    print(num3, num1, num2)
else:
    print(num3, num2, num1)