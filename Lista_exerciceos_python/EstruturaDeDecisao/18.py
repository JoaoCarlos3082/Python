# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))

if dia >= 1 and dia <= 31:
    if mes >= 1 and mes <=12:
        print(f'{dia}/{mes}/{ano}')
    else:
        print('Mes invalido')    
else:
    print('Dia invalido')