# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

maior = 0
menor = 99999999999999999999999999999
num_aluno_maior = num_aluno_menor = 0

for i in range(1, 5):
    altura = float(input(f'Altura do aluno {i}: '))

    if altura > maior:
        maior = altura
        num_aluno_maior = i
        
    if altura < menor:
        menor = altura
        num_aluno_menor = i


print(num_aluno_maior, maior)  
print(num_aluno_menor, menor)      



