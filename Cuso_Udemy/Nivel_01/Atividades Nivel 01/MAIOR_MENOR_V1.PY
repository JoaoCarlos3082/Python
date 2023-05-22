
primeiro_valor = int(input('digite o primeiro valor: '))
segundo_valor = int(input('digite o segundo valor: '))

if primeiro_valor > segundo_valor:
    print(f'Primeiro valor {primeiro_valor} é o maior que o valor {segundo_valor}')

elif segundo_valor > primeiro_valor:
    print(f'Segundo valor {segundo_valor} é o maior que o valor {primeiro_valor}')

else:
    print(f'Os valors {primeiro_valor} é {segundo_valor} são iguais.')

