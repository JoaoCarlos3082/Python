
while True:
    
    valor1 = input('Valor 01: ')
    valor2 = input('Valor 02: ')
    operador = input('Qual operador ( + | - | * | / ): ')

    valor_permitido = None
    operador_valido = '+-*/'

    try:
        valor_float01 = float(valor1)
        valor_float02 = float(valor2)
        valor_permitido = True

    except:
        valor_permitido = None
        print('Valores não permitido.')
        continue    

    if operador not in operador_valido:
        print('Operador Invalido ou coloque sem spaços.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador sem spaços.')
        continue        

    if operador == '+':
        print(f'A soma dos Valores {valor_float01} + {valor_float01} = {valor_float01 + valor_float01} ')

    elif operador == '-':
        print(f'A subetração dos valores {valor_float01} - {valor_float02} = {valor_float01 - valor_float02} ')

    elif operador == '*':
        print(f'A multiplicação dos valores {valor_float01} * {valor_float02} = {valor_float01 * valor_float02} ')

    elif operador == '/':
        print(f'A divisão dos valoes {valor_float01} / {valor_float02} = {valor_float01 / valor_float02} ')

    sair = input('[S]air ou [C]ontinuar: ').lower()[0]

    if sair == 's':
        break