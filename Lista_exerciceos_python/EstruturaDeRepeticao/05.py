#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

a = float(input('População A: '))

b = float(input('Pupulação B: '))

taxa_a = float(input('Taxa de crecimento anual A: '))
taxa_b = float(input('Taxa de crecimento anual B: '))

while True:
    crecimento_a = (a * taxa_a) / 100

    crecimento_b = (b * taxa_b) / 100

    a += crecimento_a

    b += crecimento_b

    if a == b:
        print(f'{a:.1f} A = B {b:.1f}')
        break
    elif a > b:
        print(f'{a:.1f} A > B {b:.1f}')
        break    