# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

numero_turmas = int(input('Numero de turmas: '))
total_alunos = 0

for i in range(1, numero_turmas+1):
    alunos = int(input(f'Quantidade de alunos na turma {i}: '))
    if alunos > 40:
        print('A turma não pode ter mais de 40 alunos')

    else:    
        total_alunos += alunos

print(total_alunos)

media = total_alunos / numero_turmas 

print(media)