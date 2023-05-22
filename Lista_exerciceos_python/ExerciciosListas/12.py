# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


idade_alunos = [10, 20, 31, 14, 15, 16, 13, 11, 19, 21]

altura_alunos = [1.67, 1.98, 1.78, 1.71, 1.69, 1.68, 1.65, 1.56, 1.73, 1.88]

media = sum(altura_alunos) / 10
print(media)

aluno_inferior_media = []
media_do_aluno_inferior = []

cont = 0
for i in range(len(idade_alunos)):
    if idade_alunos[i] > 13:
        if altura_alunos[i] < media:
            aluno_inferior_media.append(idade_alunos[i])
            media_do_aluno_inferior.append(altura_alunos[i])
            cont += 1

print(cont)
print(aluno_inferior_media)
print(media_do_aluno_inferior)        