# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:    
    nota = int(input('Nota entre 0 e 10: '))

    if nota >= 0 and nota <= 10:
        print('Nota valida')
        break
    else:
        print('Nota invalida')
       
