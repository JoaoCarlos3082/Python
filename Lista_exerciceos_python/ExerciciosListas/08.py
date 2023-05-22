# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

for c in range(5):
    altura = float(input(f'Altura da pessoa {c}: '))
    idade = int(input(f'Idade da pessoa {c}: '))
    idades.append(idade)
    alturas.append(altura)

idades.reverse()
alturas.reverse()

print(idades, alturas)
