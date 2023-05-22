valor1 = int(input('Valor 01: '))

valor2 = int(input('Valor 02: '))

soma = valor1 + valor2

multi = valor1 * valor2

sub = valor1 - valor2

div = valor1 / valor2

print('+-='*10)

print('[1] Somar')
print('[2] subetração')
print('[3] multiplicação')
print('[4] divisão')
opc = int(input('Qual a opeção? '))

print('+-='*10)

if opc == 1:
    print(f'Soma dos valores {valor1} + {valor2} = {soma}')

elif opc == 2:
    print(f'A subetração dos valors {valor1} - {valor2} = {sub}')

elif opc == 3:
    print(f'A multiplicação dos valors {valor1} * {valor2} = {multi}')

elif opc == 4:
    print(f'A divisão dos valores {valor1} / {valor2} = {div}')

else:
    print('opc e não e valida')                