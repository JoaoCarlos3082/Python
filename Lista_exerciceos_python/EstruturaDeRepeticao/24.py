notas = []

while True:
    nota = float(input('nota: '))
    notas.append(nota)

    if nota == 999:
        notas.pop()
        break

media = (sum(notas)) / len(notas)    

print(media)