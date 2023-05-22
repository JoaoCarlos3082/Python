# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

alunos = []
medias = []

media = 0
total_nota = 0

for i in range(1, 5):
    total_nota = 0
    media = 0
    for c in range(1, 5):
        nota = float(input(f'Nota {c} do aluno {i}: '))
        total_nota += nota
    media = total_nota / 4
    medias.append(media)  
    alunos.append(i) 

for i in range(len(alunos)):
    print(f'A media do aluno {alunos[i]} foi de {medias[i]}')    

