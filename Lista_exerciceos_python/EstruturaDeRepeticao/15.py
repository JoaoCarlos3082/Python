# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input("Digite o número de termos desejado: "))
fibonacci = [1, 1]

while len(fibonacci) < n:
    # Calcula o próximo termo da série
    proximo_termo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_termo)

# Exibe a série de Fibonacci gerada
print(f"Série de Fibonacci até o {n}º termo:")
for termo in fibonacci:
    print(termo, end=" ")