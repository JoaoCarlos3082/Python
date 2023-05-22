# TRY -> tentar
# EXCEPT -> se tiver erro

numero_str = input('Dobra um numero digitado: ')

try:
    print(f'numero str: {numero_str}')
    numero_int = int(numero_str)
    print(f'O dobro do numero {numero_int} é {numero_int * 2}')

except:
    print('Isso não e um numero:')

