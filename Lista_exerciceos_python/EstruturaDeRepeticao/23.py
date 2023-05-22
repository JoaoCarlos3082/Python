# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.


n = int(input("Digite um número inteiro: "))

primos = []
num_divisoes = 0

for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        num_divisoes += 1
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primos.append(num)

print("Os números primos entre 1 e", n, "são:", primos)
print("Número de divisões executadas:", num_divisoes)