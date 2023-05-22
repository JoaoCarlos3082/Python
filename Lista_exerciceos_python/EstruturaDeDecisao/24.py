#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
"""
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

def frase_numero(calc):
    if calc % 2 == 0:
        print(f'O resultado, {calc} é Par.')
    
    elif calc % 2 == 1:
        print(f'O resultado, {calc} é Impar.')

    if calc > 0:
        print(f'O resultado {calc} é positivo.')

    if calc < 0:
        print(f'O resultado {calc} é negativo.')      

    if calc.is_integer():  
        print(f'O resultado {calc} é numero inteiro')  

    else:
        print(f'O resultado {calc} é decimal')



num1 = float(input('Numero 01: '))
num2 = float(input('Numero 02: '))

print()
print('+=-'*10)
print()

print('Somar [1]')
print('Subtrair [2]')
print('Dividir [3]')
print('Multiplicar [4]')

print()
print('+=-'*10)
print()

opc = int(input('Qual o operação: '))

if opc == 1:
    calc = num1 + num2
    frase_numero(calc)

elif opc == 2:
    calc = num1 - num2
    frase_numero(calc)

elif opc == 3:
    calc = num1 / num2
    frase_numero(calc)

elif opc == 4:
    calc = num1 * num2
    frase_numero(calc)

else:
    print('Opeção invalida')            

