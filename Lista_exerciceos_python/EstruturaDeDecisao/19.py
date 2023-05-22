# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
"""
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 
"""

numero = 32
numero_str = str(numero)
numero_str_invertido = numero_str[::-1]
cont = 0

if numero <= 1000:
    if cont in range(len(numero_str_invertido)):
        print(f'{numero_str_invertido[cont]} unidades')
        cont += 1    
        if cont in range(len(numero_str_invertido)):
            print(f'{numero_str_invertido[cont]} dezenas')
            cont += 1
            if cont in range(len(numero_str_invertido)):
                print(f'{numero_str_invertido[cont]} centenas')
                
            
