'''Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35'''

while True:

    num = int(input('Numero: '))
    inicio = int(input('Inicio da tabuada: '))
    fim = int(input('Fim da tabuada: '))

    if fim < inicio:
        print('O valor final não pode ser maior que o inicial.')

    else:    
        for i in range(inicio, fim+1):
            print(f'{num} X {i} = {num * i}')
        break

    




    