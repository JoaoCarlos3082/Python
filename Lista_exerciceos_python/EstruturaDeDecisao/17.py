# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = 2400
igual_a_zero_por_4 = ano % 4
igual_a_zero_por_100 = ano % 100
igual_a_zero_por_400 = ano % 400

if igual_a_zero_por_4 == 0:    
    if igual_a_zero_por_100 == 0:
        if igual_a_zero_por_400 == 0:
            print(f'O ano {ano} é bixesto')

        else: 
            print(f'O ano {ano} não e bixesto')  

    elif igual_a_zero_por_100 != 0:
        print(f'O ano {ano} é bixesto')

elif igual_a_zero_por_4 != 0:
    print(f'O ano {ano} não e bixesto')