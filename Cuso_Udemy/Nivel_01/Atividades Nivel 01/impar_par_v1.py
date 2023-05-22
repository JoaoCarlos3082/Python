
'''
try:
    numero_str = input ('digite um numero inteiro: ')
    numero_inteiro = int(numero_str)
    
    if (numero_inteiro % 2) == 0:
        print(f'Numero {numero_inteiro} é par')

    elif (numero_inteiro % 2) == 1:
        print(f'Numero {numero_inteiro} é impar')

    else:
        print('isso não e numero inteiro')
except:
    print('Isso não e numero inteiro.')

'''

numero = input('Digite um numero Inteiro: ')
numero_inteiro = ''

if numero.isdigit():
    numero_inteiro = int(numero)

    if (numero_inteiro % 2) == 0:
        print(f'Numero {numero_inteiro} é par')

    elif (numero_inteiro % 2) == 1:
        print(f'Numero {numero_inteiro} é impar')

else:
    print('Isso não e um numero inteiro')



