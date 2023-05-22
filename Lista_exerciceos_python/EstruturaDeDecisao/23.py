# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.



numero = float(input('Numero: '))

if numero.is_integer():
    print(f'Numero inteiro, {numero}')

else:
    print(f'Numero decimal, {numero}')
    print(f'Aredondado o numero decimal {round(numero)}')    