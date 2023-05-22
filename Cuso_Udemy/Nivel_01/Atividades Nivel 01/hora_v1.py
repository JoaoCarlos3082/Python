
hora_str = input(('Quantas horas: '))
minutos_str = input(('Quantos minutos: '))

if hora_str.isdigit() and minutos_str.isdigit():
    hora = int(hora_str)
    minutos = int(minutos_str)
    
    if hora <=24 and minutos <=60:

        if hora <=11:
            print(f'bom dia são {hora}:{minutos}')

        elif hora <= 17:
            print(f'boa tarde são {hora}:{minutos}')

        elif hora <= 24:
            print(f'boa noite são {hora}:{minutos}')

    else:
        print('isso não é um horario valido.')   

else:
    print(f'ERRO!, Os horariso informados não sao validos {hora_str}:{minutos_str}')        

    