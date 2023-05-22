# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
'''
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

x = 1988
y = 100
resto = x % y
print(resto)

delta = 0

a = float(input('A: '))

if a == 0:
    print('Não e uma esquação de segundo grau')

else:  
    b = float(input('B: '))

    c = float(input('C: '))

    delta = (b**2) - (4 * a * c)

    if delta < 0:
        print(f'Com o delta negativo "{delta}" a equação não tem raizes reais')

    elif delta == 0:
        print((-b) / (2*a))
      
    else:
        print(delta)
        print(f'X1: {(-(b) + ((delta** 0.5))) / (2 * a)}')
        print(f'X1: {(-(b) - ((delta** 0.5))) / (2 * a)}')  

'''
while True:
    a = float(input('A: '))

    if a == 0:
        print('Não é uma equação de segunda grau')
        break

    b = float(input('B: '))

    c = float(input('C: '))

    delta = (b**2) - (4 * a * c)

    if delta < 0:
        print(f'Com o delta negativo "{delta}" a equação não tem raizes reais')
        break

    elif delta == 0:
        print((-b) / (2*a))
        break

    else:
        print(delta)
        print(f'X1: {(-(b) + ((delta** 0.5))) / (2 * a)}')
        print(f'X1: {(-(b) - ((delta** 0.5))) / (2 * a)}')
        break
    '''

    