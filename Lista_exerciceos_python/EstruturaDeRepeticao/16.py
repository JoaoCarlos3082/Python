# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.



fibonacci = [1, 1]

while True:
    # Calcula o próximo termo da série
    proximo_termo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_termo)
    if fibonacci[-1] > 500:
        break

# Exibe a série de Fibonacci gerada
print(f"Série de Fibonacci até o {len(fibonacci)}º termo:")
for termo in fibonacci:
    print(termo, end=" ")