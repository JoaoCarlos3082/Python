# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = 24
divisores = []

if num < 2:
    print(num, "não é primo")
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            divisores.append(i)
    if divisores:
        print(num, "não é primo e é divisível por", 1, "e", num)
        for divisor in divisores:
            print(divisor)
    else:
        print(num, "é primo")
